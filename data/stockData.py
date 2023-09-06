import pandas as pd
import data.stock.getDataByTushare as getByTs
import data.stock.getDataByLocal as getByLoc
import data.stock.saveDataToLocal as saveToLoc

def daily(code,startDay,endDay):
    """
    先从本地获取，如果没有从tushare获取,并且调用saveToLoc存储到本地
    :param code: 代码
    :param startDay:开始日期
    :param endDay: 结束日期
    :return: df类型数据
    """
    try:
        return getByLoc.daily(code, startDay, endDay)
    except:
        saveToLoc.daily(code,startDay,endDay)
        return getByTs.daily(code, startDay, endDay)

def weekly(code,startDay,endDay):
    """
      先从本地获取，如果没有从tushare获取,并且调用saveToLoc存储到本地
      :param code: 代码
      :param startDay:开始日期
      :param endDay: 结束日期
      :return: df类型数据
      """
    try:
        return getByLoc.weekly(code, startDay, endDay)
    except:
        saveToLoc.weekly(code,startDay,endDay)
        return getByTs.weekly(code,startDay,endDay)

def monthly(code,startDay,endDay):
    """
      先从本地获取，如果没有从tushare获取,并且调用saveToLoc存储到本地
      :param code: 代码
      :param startDay:开始日期
      :param endDay: 结束日期
      :return: df类型数据
      """
    try:
        return getByLoc.monthly(code, startDay, endDay)
    except:
        saveToLoc.monthly(code,startDay,endDay)
        return getByTs.monthly(code, startDay, endDay)

def stockList():
    """
    all stock name, code,startDay,endDay
    :return:
    """
    pass
if __name__=='__main__':
    df = daily("000058.SZ",'20230202','20230210')
    print(df)


