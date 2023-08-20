import pandas as pd
import data.stock.getDataByTushare as getByTs
import data.stock.getDataByLocal as getByLoc

def daily(code,startDay,endDay):
    """
    先从本地获取，如果没有从tushare获取
    :param code: 代码
    :param startDay:开始日期
    :param endDay: 结束日期
    :return: df类型数据
    """
    try:
        return getByLoc.daily(code, startDay, endDay)
    except:
        return getByTs.daily(code, startDay, endDay)


def weekly(code,startDay,endDay):
    """
      先从本地获取，如果没有从tushare获取
      :param code: 代码
      :param startDay:开始日期
      :param endDay: 结束日期
      :return: df类型数据
      """
    try:
        return getByLoc.weekly(code, startDay, endDay)
    except:
        return getByTs.weekly(code,startDay,endDay)

def monthly(code,startDay,endDay):
    """
      先从本地获取，如果没有从tushare获取
      :param code: 代码
      :param startDay:开始日期
      :param endDay: 结束日期
      :return: df类型数据
      """
    try:
        return getByLoc.monthly(code, startDay, endDay)
    except:
        return getByTs.monthly(code, startDay, endDay)


if __name__=='__main__':
    df = daily("000058.SZ",'20230101','20230202')
    print(df)
