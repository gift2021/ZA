#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create two horizontal
toolbars.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddTool(wx.ID_UNDO, '', wx.Bitmap('tundo.png'))
        tredo = self.toolbar.AddTool(wx.ID_REDO, '', wx.Bitmap('tredo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('texit.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

        self.SetSize((350, 250))
        self.SetTitle('Undo redo')
        self.Centre()

    def OnUndo(self, e):
        if self.count > 1 and self.count <= 5:
            self.count = self.count - 1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >= 1:
            self.count = self.count + 1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)


    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
   # print(wx.lib.delayedresult.__version__)


if __name__ == '__main__':
    import tushare as ts
    import wx
    import matplotlib.pyplot as plt
    import wx.lib.delayedresult as delay
    import six

    token = '303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041'  # 在Tushare网站上注册并获取API token
    ts.set_token(token)
    pro = ts.pro_api()


    def fetch_kline():
        token = '303ece62497562396a9420fb0a36201d99f1ba1bd6c7713391a5a041'  # 在Tushare网站上注册并获取API token
        ts.set_token(token)
        pro = ts.pro_api()
        symbol = '000001.SZ'  # 股票代码
        start_date = '2023-01-01'  # 开始日期
        end_date = '2023-03-17'  # 结束日期
        ktype = '1min'  # K线类型，这里使用1分钟K线
        df = pro.daily(ts_code=symbol, start_date=start_date, end_date=end_date)
        print(df)
        return df[['open', 'close']]  # 返回需要的列数据，根据实际情况调整代码


    def process_result(result):
        if result.result:
            data = result.result[0]  # 取第一个股票的K线数据，根据实际情况调整代码
            plot_kline(data)
        else:
            print('Failed to fetch K line data.')
        frame.Close()  # 关闭窗口


    def plot_kline(data):
        plt.figure(figsize=(10, 6))
        plt.plot(data['open'], label='Open Price')
        plt.plot(data['close'], label='Close Price')
        plt.title('K Line Data')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()


    app = wx.App()
    frame = wx.Frame(None, title='K线数据展示', size=(800, 600))
    result = delay.startWorker(fetch_kline, process_result)  # 在后台异步执行fetch_kline函数，并将结果传递给process_result函数处理
    frame.Show()  # 显示窗口
    app.MainLoop()  # 进入主循环，等待处理结果并更新界面
