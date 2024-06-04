import tushare as ts



ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
# ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
pro = ts.pro_api()

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


def bkt(ts_code,start_date,end_date,buy,sell):
    # todo 将df以数据或者类传入，自己再调用费资源   def btk(dataframe df,buy,sell)
    '''
    简单回测系统，输入代码，开始，结束日期，买入价，卖出价，返回回测收益，模拟资金10w，无手续费,全仓买入模式
    :param ts_code:股票代码
    :param start_date:开始交易日期
    :param end_date:结束交易日期
    :param buy:买入价
    :param sell:卖出价
    :return:交易记录，获利
    '''

    # 返回record 记录交易记录
    # 格式：time
    record = ''

    #hold=1为持有，-1为未持有
    hold = -1

    #初始收益为0
    benfite = 0

    #初始本金为10w
    num = 100000

    #股票数量
    stack_num = 0
    price = 0

    # 交易次数
    flag = 0

    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)



    min1 = 10000
    max1 = 0

    for i in range(len(df)-1,-1,-1):
        # df.iloc[i,2]好像是开盘价，还不是最低价
        price1 = df.iloc[i, 2]
        if max1 < price1:
            max1 = price1
        if min1 > price1:
            min1 = price1

    list = []
    add_price = (max1-min1)/5
    for i in range(5):
        list.append(round(min1+add_price*i))

    list.append(max1)
    # todo 再这个系统内实现单个股票均值回归收益最高的买卖区间，再写一个函数吧，这个是开山版，保留住，还是在这基础上改



    for i in range(len(df)-1,-1,-1):
        price = df.iloc[i, 2]
        if price >= sell:
            if hold == 1:
                num = num + stack_num*price
                flag += 1
                record += str(flag) + ':sell   time:' + df.iloc[i,1] + '   price:' + str(price) + '\n'
                stack_num = 0
                hold = -hold

        else:
            if price <= buy:
                if hold == -1:
                    stack_num = (num//(price*100))*100
                    num = num - stack_num * price
                    hold = -hold
                    flag += 1
                    record += str(flag) + ':buy   time:' + df.iloc[i, 1] + '   price:' + str(price) + '   stockNum    ' +str(stack_num) + '\n'
    profit = round(num + stack_num*price -100000)
    return record,profit,list


if __name__ == '__main__':
    record,profit,list= bkt('000020.SZ','20230101', '20240601',11.118,13.315999999)
    print(record)
    print(profit)
    print(list)

