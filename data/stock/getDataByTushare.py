import tushare as ts
import pandas as pd

ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
# ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
pro = ts.pro_api()

def getStockDailY(ts_code,start_date,end_date):
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    return df
def getStockWeekly():
    pass

def getStockMonthly():
    pass


if __name__=="__main__":
    print(getStockDailY("000058.SZ",'20200202','20200303'))
