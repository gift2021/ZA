
import tushare as ts
import requests
import urllib.request
import pprint
import csv

import pandas as pd
#多，低价买入，高价卖出
def bull(buy,sell):
    # ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
    ts.set_token('303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041')
    # ts.set_token('6a340aafdbb9232fbbbab2adf6ec0350bd70bfd87a6bf588972b323e')
    pro = ts.pro_api()
    df = pro.daily(ts_code='000058.SZ', start_date='20180101', end_date='20221230')
    hold = -1
    #hold=1为持有，-1为未持有
    benfite = 0
    #初始收益为0
    num = 100000
    #初始本金为10w
    stack_num = 0
    #股票数量
    flag = 0
    for i in range(len(df)-1,-1,-1):
        price = df.iloc[i, 2]
        if price >= sell:
            if hold == 1:
                num = num + stack_num*price
                stack_num = 0
                hold = -hold
                print("sell   time:",df.iloc[i,1],"  price: ",price)
                flag += 1
                print(flag,num)
                print("")

        else:
            if price <= buy:
                if hold == -1:
                    stack_num = (num//(price*100))*100
                    num = num - stack_num * price
                    hold = -hold
                    print("buy   time:", df.iloc[i, 1], "  price: ", price,"stockNum:  ",stack_num)

    print(num,stack_num)

if __name__ == '__main__':
    bull(5.5,6.5)
    # pro = ts.pro_api()
    #
    # df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
    #
    # # print(df)
    # df.to_csv('app/try.csv')
    #
    # read_csv = pd.read_csv("app/try.csv")
    # print(read_csv)

#buy所需要的总价
def buy(num,price):
    shoushu = num//(price*100)
    #手数100股
    num = shoushu * price *100
    return num