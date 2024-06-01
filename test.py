import backTest as bkt
import pandas as pd
import numpy as np
import priceIoc as pic

# 实现遍历所有股票最近收益，从高到低排个序



# record, profit = bkt.bkt('000058.SZ', '20180101', '20221230', 5.5, 6.5)
# print(record)
# print(profit)

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
        tradeList = pic.priceIoc(stockList.iloc[i,1],start_date,end_date,5)

        # # 对切分的价格进行遍历，查找获利最多的价格区间
        for j in range(len(tradeList)):
            max = 0
            for k in range(5-j-1):

                if(j>k+1):
                    break
                # 获取回测结果
                record , profit = bkt.bkt(str(stockList.iloc[i,1]),start_date,end_date,tradeList[j],tradeList[k+1])

                if profit>max:
                    max = profit
                    flagj = j
                    flagk = k
                    flagrecord = record
                    flagpro = profit


        bigProfitList.append([stockList.iloc[i][1],tradeList[flagj],tradeList[flagk],round(flagpro)])
        res += str(stockList.iloc[i, 1]) + '买入，卖出价   ' + str(tradeList[flagj]) + '   ' + str(tradeList[flagk + 1]) \
               + '   获利  ' + str(flagpro) + '\n' + flagrecord
        print(i)

        if(i == 1):
            break

    return res,bigProfitList

res,bigProfitList = test('20220101', '20220230')


# todo : 排序，pro变成str类型数据，排序
bigProfitList = np.delete(bigProfitList,0,axis=0)


# bigProfitList = np.array([bigProfitList[:,3].astype(int) for i in range(bigProfitList[:,3].shape[1])]).T
# bigProfitList[:,3] = bigProfitList[:,3].astype(int)
# bigProfitList[:,3] = np.asarray(bigProfitList[:,3], dtype=int)
# bigProfitList = np.array(bigProfitList, dtype=str)
# bigProfitList[:, 3] = bigProfitList[:, 3].astype(int)
# bigProfitList[:, 2] = bigProfitList[:, 2].astype(float)
# bigProfitList[:, 1] = bigProfitList[:, 1].astype(float)


new_array = [[]]
# todo   nump库是真tm难用，艹一个bug改2，3个小时，还没改好，睡觉了
new_array.append(bigProfitList[:, 0].copy())
new_array.append(bigProfitList[:, 1].copy())
new_array.append(bigProfitList[:, 2].copy())
new_array.append(bigProfitList[:, 3].astype(int))
print(new_array)
# print(type(new_array[1][3]))

# new_bigProfitList[:, 0] = bigProfitList[:, 0]  # 第一列保持原样
# new_bigProfitList[:, 1] = bigProfitList[:, 1]  # 第二列转换为float
# new_bigProfitList[:, 2] = bigProfitList[:, 2]  # 第三列保持原样
# # new_bigProfitList[:, 3] = bigProfitList[:, 3].astype(int) # 第三列保持原样
# for i in range(len(bigProfitList)):
#     new_bigProfitList[i][3] = int(bigProfitList[i][3])
#     print(type(new_bigProfitList[i][3]))
#     print(type(int(bigProfitList[i][3])))
#
# print(type(new_bigProfitList[1,0]))
# print(type(new_bigProfitList[1,1]))
# print(type(new_bigProfitList[1,2]))
# print(type(new_bigProfitList[0,3]))
# print(type(new_bigProfitList[1,3].astype(int)))


sorted_arr = new_array[new_array[:,3].argsort()]


print(sorted_arr)


