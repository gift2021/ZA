import pandas as pd

def daily(code,startDay,endDay):
    """
    从本地csv文件读取代码
    :param code: 交易代码
    :param startDay: 开始日期
    :param endDay: 结束日期
    :return: 返回以datetime为索引的df
    """
    # todo  将路径更换为/ZA/....
    try:
        path = "/ZA/data/stock/daily/" + code
        df = pd.read_csv(path,parse_dates=['trade_date'],index_col=['trade_date'])
        target_data = df.loc[startDay:endDay]
        return target_data
    except Exception as e:
        print("error:" ,e)

def weekly(code,startDay,endDay):
    """
    从本地csv文件读取代码
    :param code: 交易代码
    :param startDay: 开始日期
    :param endDay: 结束日期
    :return: 返回以datetime为索引的df
    """

    df = pd.read_csv("/ZA/data/stock/weekly/" + code,parse_dates=['trade_date'],index_col=['trade_date'])
    target_data = df.loc[startDay:endDay]
    return target_data
def monthly(code,startDay,endDay):
    """
    从本地csv文件读取代码
    :param code: 交易代码
    :param startDay: 开始日期
    :param endDay: 结束日期
    :return: 返回以datetime为索引的df
    """
    df = pd.read_csv("/ZA/data/stock/monthly/" + code,parse_dates=['trade_date'],index_col=['trade_date'])
    target_data = df.loc[startDay:endDay]
    return target_data

if __name__=='__main__':
    df = daily("000058.SZ",'20230202','20230210')
    print(df)
