import argparse


if __name__ == '__main__':

    #initiate the parser
    parser = argparse.ArgumentParser()

    parser.add_argument("--mode","-m",help="Choose service mode. flask,clipper,automml",default="flask")

    #read arguments from command line
    args = parser.parse_args()

    #assign mode value
    if args.mode:
        mode = args.mode
        print('Mode selected to serve prediction %s' % mode)

    if mode == 'flask':
        #Connect to flask API
        print('%s API predicted' % mode)


    elif mode == 'clipper':
        #Connect to clipper API
        print('%s API predicted' % mode)

    elif mode == 'automl':
        #Connect to automl API
        print('%s API predicted' % mode)

    else:
        print('wrong option selected, options are: clipper,flask,automl. example: test.py -m flask')
        
        
        
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python if_condition.py
# Mode selected to serve prediction flask
# flask API predicted
# 
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python if_condition.py -m automl
# Mode selected to serve prediction automl
# automl API predicted
# 
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python if_condition.py -m zzz
# Mode selected to serve prediction zzz
# wrong option selected, options are: clipper,flask,automl. example: test.py -m flask

