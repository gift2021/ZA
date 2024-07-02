import tushare as ts



# xxxxxxx
ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
# ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
pro = ts.pro_api()

def bkt(ts_code,start_date,end_date):
    '''
    简单回测系统，输入代码，开始，结束日期，买入价，卖出价，返回回测收益，模拟资金10w，无手续费,全仓买入模式
    :param ts_code:股票代码
    :param start_date:开始交易日期
    :param end_date:结束交易日期
    :param buy:买入价
    :param sell:卖出价
    :return:交易记录，获利
    '''
    trade = []



    df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
    min = 10000
    max = 0
    for i in range(len(df) - 1, -1, -1):
         # df.iloc[i,2]好像是开盘价，还不是最低价
        price = df.iloc[i, 2]
        if max < price:
             max = price
        if min > price:
             min = price
    list = []
    add_price = (max - min) / 5
    for i in range(5):
        list.append(min + add_price * i)

    list.append(max)

    # 返回record 记录交易记录
    # 格式：time

    maxprofit = 0

    flagrecord = ''

    flagbuyprice = 0

    flagsellprice = 0

    #初始收益为0
    benfite = 0
    # 交易次数


    for j in range(5):
        for k in range(5 - j):
            record = ''
            flag = 0
            # hold=1为持有，-1为未持有
            hold = -1
            # 初始本金为10w
            num = 100000
            # 股票数量
            stack_num = 0
            price = 0
            for i in range(len(df)-1,-1,-1):
                price = df.iloc[i, 2]
                # 卖出价格
                if price >= list[5-k]:
                    if hold == 1:
                        num = num + stack_num*price
                        flag += 1
                        record += str(flag) + ':sell   time:' + df.iloc[i,1] + '   price:' + str(price) + '\n'
                        stack_num = 0
                        hold = -hold


                else:
                    if price <= list[j]:
                        if hold == -1:
                            stack_num = (num//(price*100))*100
                            num = num - stack_num * price
                            hold = -hold
                            flag += 1
                            record += str(flag) + ':buy   time:' + df.iloc[i, 1] + '   price:' + str(price) + '   stockNum    ' +str(stack_num) + '\n'
            profit = round(num + stack_num*price -100000)
            if(maxprofit < profit):
                flagbuyprice = list[j]
                flagsellprice = list[5-k]
                maxprofit = profit
                flagrecord = record
    trade.append(ts_code)
    trade.append(round(flagbuyprice,2))
    trade.append(round(flagsellprice,2))
    trade.append(maxprofit)


    return trade,flagrecord

if __name__ == '__main__':
    trade,record = bkt('002112.SZ','20230101', '20240601')
    print(record)
    print(trade)


