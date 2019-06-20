# python_cheatsheet

import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
import os
import json
import prediction.prediction_model as prediction_model
from modelPreprocessing import model


pickle_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../data/pickle/"))
logs_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../logs"))
sql_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../sql"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "Welcome here"


@app.route('/predict', methods=['POST'])
def apicall():
    """API Call

    Pandas dataframe (sent as a payload) from API Call
    """
    try:
        test_json = request.get_json()
        #test = "{}{}{}".format("[",test_json,"]")
        data = pd.read_json(json.dumps(test_json), orient='records')
    except Exception as e:
        raise e

    if data.empty:
        return 404
    else:
        #Load the saved model
        df_final = data.copy()
        df_final.columns = [x.lower() for x in df_final.columns]
        #loan_acct_num = df_final["loan_account_num"]
        #df_final.drop("loan_account_num",inplace=True,axis=1)
        column = list(df_final.columns)
        m=model.modelPreProcessing(df_final ,mode= "predict" ,col=None)
        X_test=df_final
        m.predict_model(X_test)
        y_predict=m.voting_predict(X_test)
        y_probab=m.probab_score(X_test)

        """Add the predictions as Series to a new pandas dataframe
                                OR
           Depending on the use-case, the entire test data appended with the new files
        """
        df_final.drop(column,inplace=True,axis=1)

        df_final.loc[:,"model_prediction"]=y_predict
        df_final.loc[:,"model_probablities"]=y_probab
        #df_final.insert(loc=0, column="loan_account_num", value=loan_acct_num)
        responses = jsonify(predictions=df_final.to_json(orient="records"))
        responses.status_code = 200

        return responses


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8050)
    
    
    
    
    
    
    import argparse
import utils.sfExecutor as sfExecutor
import simplejson as json
import urllib as urllib

def main(mode):
    df = sfExecutor.get_df()
    df.columns = [x.lower() for x in df.columns]
    print(df.columns)

    df_acct = df['loan_account_num']
    df.drop(['loan_account_num'],axis=1,inplace=True)
    print(df.shape)
    for data in df.to_dict(orient='records'):
        #print(data)
        #data = str(data).replace("'",'"').replace('{','[{').replace('}','}]')
        response = predict(mode,data)
        print(response)
    #get prediction result
    #result = predict(mode,data)

        #update result in snowflake prediction table
    #sfExecutor.runsql('update table xyz')


def predict(mode, d):
    if mode == 'flask':
        url = 'http://10.206.117.80:8050/predict'
        data = json.dumps(d)
        print("")
        action = "POST"
        data = data.encode(encoding="utf-8")
        try:
            request = urllib.request.Request(url=url, method=action, data=data)
            request.add_header('Accept', 'application/json;v=1')
            request.add_header('Content-type', ' application/json')
            resp = urllib.request.urlopen(request)
            raw_data = resp.read()
            encoding = resp.info().get_content_charset('utf8')
            if not (raw_data == b''):
                data = json.loads(raw_data.decode(encoding))
            else:
                data = "Empty response from path create action *** normal ***"
            output = data
        except Exception as e:
            print("\nLockbox not found / Error in input...\n")
            print("HttpReponse : " + str(e.read()))
            print()
            exit(1)
        print(" ")
        display(output)
        print('%s API predicted' % mode)
        return 'success'

    elif mode == 'clipper':
        # Connect to clipper API
        print('%s API predicted' % mode)
        return 'api result'

    elif mode == 'mlflow':
        # Connect to mlflow API
        print('%s API predicted' % mode)
        return 'api result'

    else:
        print('wrong option selected, options are: clipper,flask,automl. example: test.py -m flask')

def display(output):
    print()
    print(
            "•••••••••••••••••••••••••••••••••••••••••••• Begin Output ••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print()
    print(json.dumps(output, indent=4))
    print()
    print(
            "•••••••••••••••••••••••••••••••••••••••••••• End Output ••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print()

if __name__ == '__main__':
    # initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", help="Choose service mode. flask,clipper,mlflow", default="flask")
    # read arguments from command line
    args = parser.parse_args()
    # assign mode value
    if args.mode:
        mode = args.mode
        print('Mode selected to serve prediction %s' % mode)
    main(mode)

# (venv) C:\Users\chitt\PycharmProjects>python if_condition.py
# Mode selected to serve prediction flask
# flask API predicted
#
# (venv) C:\Users\chitt\PycharmProjects>python if_condition.py -m mlflow
# Mode selected to serve prediction automl
# mlflow API predicted
#
# (venv) C:\Users\chitt\PycharmProjects>python if_condition.py -m zzz
# Mode selected to serve prediction zzz
# wrong option selected, options are: clipper,flask,automl. example: test.py -m flask










[loggers]
keys=root

[handlers]
keys=stream_handler,file_handler

[formatters]
keys=formatter

[logger_root]
level=DEBUG
handlers=stream_handler,file_handler

[logger_main]
level=DEBUG
handlers=stream_handler,file_handler
qualname=compiler.parser


[logger_ModelTrainPipeline]
level=DEBUG
handlers=stream_handler,file_handler
qualname=compiler.parser

[handler_stream_handler]
class=StreamHandler
level=DEBUG
formatter=formatter
args=(sys.stderr,)

[handler_file_handler]
class=FileHandler
level=DEBUG
formatter=formatter
args=('logs\\churn.log', 'a')

[formatter_formatter]
format='%(asctime)s - %(name)s - %(levelname)-4s - %(lineno)04d - %(message)s'
