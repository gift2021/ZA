import backTest as bkt
import pandas as pd
import numpy as np
import priceIoc as pic

# 实现遍历所有股票最近收益，从高到低排个序

df = pd.read_csv('D:\ZA\data\stock\stockList.csv')
stockList = pd.DataFrame(df)

bigProfitList = [['000001.SZ',16.21,16.21,4085]]



def test(start_date,end_date):
    '''
    回测收益，按照高买低卖价格区间操作，价格区间切分5
    :param start_date: 开始时间
    :param end_date: 结束时间
    :return: 返回结果，什么类型数据比较好
    '''
    res = ''
    flagj = 0
    flagk = 0
    flagrecord = ''
    flagpro = 0
    for i in range(len(stockList)):
        # 买入和卖出价在一个列表中，对日期内价格进行切分
        # todo 这里调用一次接口，计算价格区间
        tradeList = pic.priceIoc(stockList.iloc[i,1],start_date,end_date,5)

        if (sum(tradeList)/5) > 20:
            continue

        # # 对切分的价格进行遍历，查找获利最多的价格区间
        for j in range(len(tradeList)):
            max = 0
            for k in range(5-j-1):

                if(j>k+1):
                    break
                # 获取回测结果
                # todo 这里调用一次接口
                record , profit = bkt.bkt(str(stockList.iloc[i,1]),start_date,end_date,tradeList[j],tradeList[k+1])

                if profit>max:
                    max = profit
                    flagj = j
                    flagk = k
                    flagrecord = record
                    flagpro = profit


        bigProfitList.append([stockList.iloc[i][1],tradeList[flagj],tradeList[flagk],round(flagpro)])
        res += str(stockList.iloc[i, 1]) + '  买入，卖出价   ' + str(round(tradeList[flagj],2)) + '     ' + str(round(tradeList[flagk + 1],2)) \
               + '      获利      ' + str(flagpro) + '\n'

        if(i == 500):
            break
        print(i)
    return res,bigProfitList

res,bigProfitList = test('20230101', '20240601')
bigProfitList = pd.DataFrame(bigProfitList)

bigProfitList = bigProfitList.drop(0)

bigProfitList.sort_values(by=bigProfitList.columns[3], ascending=False, inplace=True)
print(bigProfitList)
bigProfitList.to_csv('output.csv', index=False)  # 保存到CSV文件
# todo  将排序后的交易记录拿出来，怎么存储是一个问题

# 先跑个100股，看看效果




