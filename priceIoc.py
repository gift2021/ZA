import backTest as bkt
import tushare as ts



ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
# ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
pro = ts.pro_api()
# 解决价格区间问题，之前做过这个问题，可以对价格进行切分，具体某段时间，多个价格间隔，计算震荡价格最优解
# 震荡交易，区间间波动，低买高卖

# 实现对价格的切分，看切分程度，越细，交易获利可能越大，maybe
def just(ts_code,start_date,end_date):
    '''
    :param ts_code: 股票代码
    :param start_date: 开始日期
    :param end_date: 结束日期
    :return: 返回 min，max，最小值，最大值
    '''
    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    min = 10000
    max = 0

    for i in range(len(df)-1,-1,-1):
        # df.iloc[i,2]好像是开盘价，还不是最低价
        price = df.iloc[i, 2]
        if max < price:
            max = price
        if min > price:
            min = price
    return min,max

def priceIoc(ts_code,start_date,end_date,n):
    '''
    :param ts_code:
    :param start_date:
    :param end_date:
    :param n: 切分的段，1不切分，2切分为两个价格区间
    :return: 返回一个什么类型数据比较好，数组吗，相邻的两个
    '''
    min,max = just(ts_code,start_date,end_date)

    list = []
    add_price = (max-min)/n
    for i in range(n):
        list.append(min+add_price*i)

    list.append(max)

    return list
# print(priceIoc('000058.SZ','20180101','20221230',5))




