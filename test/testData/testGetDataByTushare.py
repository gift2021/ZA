from data.stock.getDataByTushare import *
if __name__=='__main__':
    df = getStockDailY('0000058.SZ',20200202,20200303)
    print(df)