import data.stock.getDataByTushare as getByTs

def daily(code,startDay,endDay):
    try:
        df = getByTs.daily(code,startDay,endDay)
        df.to_csv('/ZA/data/stock/daily/' + code)
    except Exception as e:
        print("error:", e)


def weekly(code,startDay,endDay):
    try:
        df = getByTs.weekly(code, startDay, endDay)
        df.to_csv('weekly/' + code)
    except Exception as e:
        print("error:", e)


def monthly(code,startDay,endDay):
    try:
        df = getByTs.monthly(code, startDay, endDay)
        df.to_csv('monthly/' + code)
    except Exception as e:
        print("error:", e)

def saveDataToCsv(path,name):
    pass

def saveTradeDay():
    pass
#todo 存储交易数据，存在哪里，怎么存，回测数据


if __name__=='__main__':
    daily('000058.SZ','20230101','20230210')