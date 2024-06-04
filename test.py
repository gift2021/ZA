import backTest as bkt
import pandas as pd
import numpy as np
import priceIoc as pic

# 实现遍历所有股票最近收益，从高到低排个序

df = pd.read_csv('D:\ZA\data\stock\stockList.csv')
stockList = pd.DataFrame(df)

bigProfitList = [[]]

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
        # bigProfitList[i] = bkt.bkt(str(stockList.iloc[i, 1]),'20230101', '20240601')
        bigProfitList.append(bkt.bkt(str(stockList.iloc[i, 1]),'20230101', '20240601'))
        if (i > 4500):
            break
        print(i)
    return bigProfitList

bigProfitList = test('20230101', '20240601')

print(bigProfitList)


bigProfitList = pd.DataFrame(bigProfitList)

bigProfitList = bigProfitList.drop(0)

bigProfitList.sort_values(by=bigProfitList.columns[3], ascending=False, inplace=True)
print(bigProfitList)
bigProfitList.to_csv('output.csv', index=False)  # 保存到CSV文件





