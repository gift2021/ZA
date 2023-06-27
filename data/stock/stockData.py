import pandas as pd

"""
各个数据类型示例
"""
class stockDaily:
    # ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount
    columns = ['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close', 'change',
               'pct_chg', 'vol', 'amount']
    df = pd.DataFrame(columns=columns)
    """
    数据示例
    
    , ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount
    0, 000001.SZ, 20180718, 8.75, 8.85, 8.69, 8.7, 8.72, -0.02, -0.23, 525152.77, 460697.377
    1, 000001.SZ, 20180717, 8.74, 8.75, 8.66, 8.72, 8.73, -0.01, -0.11, 375356.33, 326396.994
    2, 000001.SZ, 20180716, 8.85, 8.9, 8.69, 8.73, 8.88, -0.15, -1.69, 689845.58, 603427.713
    """

class stockList:
    pass

class stockweekly:
    pass



if __name__ == '__main__':
    t = stockDaily()
    print(t.df)


