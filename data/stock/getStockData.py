from data.stock.getDataByMongodb import *
from data.stock.getDataByTushare import *
"""
调用此模块函数，返回相应的数据
"""
def getStockDaily():
    if getStockDailY("00",0,0):
        pass
    else:getdaily()

def getStockWeekly():
    if getStockWeekly():
        pass
    else:pass

pass