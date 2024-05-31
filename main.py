import data.stockData as data



#todo 完善所有的股票数据本地化，python爬虫获取，保存到mongodb中，也许不需要，自己用的，这么专业干什么


if __name__ == '__main__':

    df = data.daily("000058.SZ", '20230202', '20230210')

    print(df)
