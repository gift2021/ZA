import pandas as pd

def daily(code,startDay,endDay):
    read_csv = pd.read_csv("daily/" + code + ".csv")

    return read_csv
def weekly(code,startDay,endDay):

    read_csv = pd.read_csv("data/stock/weekly/" + code)
    return read_csv
def monthly(code,startDay,endDay):

    read_csv = pd.read_csv("data/stock/monthly/" + code)
    return read_csv


if __name__=='__main__':

    df = daily("000058.SZ",'20230101','20230202')
    print(df)
