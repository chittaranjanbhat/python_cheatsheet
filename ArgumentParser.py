import argparse

if __name__ == '__main__':

    # initiate the parser
    parser = argparse.ArgumentParser()

    # add long and short argument
    parser.add_argument("--n_value", "-n", help="set n_estimators",default=[1,1,1,1])
    parser.add_argument("--max_width", "-width", help="set maximum width", default=[2, 2, 2, 2])

    # read arguments from the command line
    args = parser.parse_args()

    # check for --width
    if args.n_value:
        print("set n_estimators values to %s" % args.n_value)
        n_estimators = list(args.n_value)
        print(type(n_estimators))
    if args.max_width:
        print("set maximum width to %s" % args.max_width)


# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python ArgumentParser.py -h
# usage: ArgumentParser.py [-h] [--n_value N_VALUE] [--max_width MAX_WIDTH]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --n_value N_VALUE, -n N_VALUE
#                         set n_estimators
#   --max_width MAX_WIDTH, -width MAX_WIDTH
#                         set maximum width
#
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python ArgumentParser.py -n [10,10,10,10]
# set n_estimators values to [10,10,10,10]
# <class 'list'>
# set maximum width to [2, 2, 2, 2]
#
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python ArgumentParser.py -n [10,10,10,10] -width [20,20,20,20]
# set n_estimators values to [10,10,10,10]
# <class 'list'>
# set maximum width to [20,20,20,20]
#
# (venv) C:\Users\chitt\PycharmProjects\Google_what_if>python ArgumentParser.py
# set n_estimators values to [1, 1, 1, 1]
# <class 'list'>
# set maximum width to [2, 2, 2, 2]
