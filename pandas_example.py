import pandas as pd

def main():
    list1=[(1,2,3),(1,2,3),(1,2,3)]
    col = ['c1','c2','c3']
    df = pd.DataFrame(list1,columns=col)
    df_c1 = df['c1']
    print(df_c1)

    cols = ['c2', 'c3', 'c4']
    lst = []
    for a in range(3):
        lst.append([2, 3, 4])

    df1 = pd.DataFrame(lst,columns=cols)
    df1['c1'] = df_c1
    print(df1)

if __name__ == '__main__':
    main()
