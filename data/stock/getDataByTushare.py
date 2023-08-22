import tushare as ts

ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
# ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
pro = ts.pro_api()

def daily(ts_code,startDay,endDay):
    df = pro.daily(ts_code=ts_code, start_date=startDay, end_date=endDay)
    return df

def weekly(ts_code,startDay,endDay):
    df = pro.weekly(ts_code=ts_code, start_date=startDay, end_date=endDay,
                    fields='ts_code,trade_date,open,high,low,close,vol,amount')
    return df

def monthly(ts_code,startDay,endDay):
    df = pro.monthly(ts_code=ts_code, start_date=startDay, end_date=endDay,
                     fields='ts_code,trade_date,open,high,low,close,vol,amount')
    return df


if __name__=='__main__':
    df = weekly("000058.SZ",'20230101','20230202')
    print(df)