import wx

class MyWindow(wx.Panel):

    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)

        self.color = '#b3b3b3'

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, e):

        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, e):

        self.Refresh()

    def OnSetFocus(self, e):

        self.color = '#ff0000'
        self.Refresh()

    def OnKillFocus(self, e):

        self.color = '#b3b3b3'
        self.Refresh()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):

        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.RIGHT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])


        self.SetSizer(grid)

        self.SetSize((350, 250))
        self.SetTitle('Focus event')
        self.Centre()


    def OnMove(self, e):

        print(e.GetEventObject())
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    import wx


    class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(600, 800))

            # 创建一个水平的 BoxSizer，用于容纳左侧的垂直 BoxSizer (vbox) 和右侧的其他内容
            hbox = wx.BoxSizer(wx.HORIZONTAL)

            # 创建一个垂直的 BoxSizer，用于容纳按钮
            vbox = wx.BoxSizer(wx.VERTICAL)

            # 创建一个 wx.Panel 用于设置背景颜色
            panel1 = wx.Panel(self)
            panel1.SetBackgroundColour(wx.Colour(200, 200, 255))  # 设置背景颜色为蓝色

            # 添加多个按钮到垂直 BoxSizer (vbox) 中
            button1 = wx.Button(panel1, label='Button 1')
            button2 = wx.Button(panel1, label='Button 2')
            button3 = wx.Button(panel1, label='Button 3')

            vbox.Add(button1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            vbox.Add(button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            vbox.Add(button3, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

            # 设置容器离顶部 10 像素，离底部 500 像素
            vbox.Add((-1, 10))  # 顶部 10 像素的间隔
            vbox.Add((-1, 500))  # 底部 500 像素的间隔

            # 添加垂直间隔，使按钮向上移动
            vbox.Add((-1, 10))  # 用于在按钮上方创建一些空白

            # 将垂直 BoxSizer (vbox) 添加到 wx.Panel 中
            panel1.SetSizer(vbox)

            # 添加 panel1 到 hbox
            hbox.Add(panel1, proportion=0, flag=wx.EXPAND | wx.ALIGN_TOP | wx.ALL)
            #         hbox.Add(vbox, proportion=0, flag=wx.EXPAND | wx.ALIGN_TOP | wx.ALL, border=10)

            # 创建右侧的 panel
            panel = wx.Panel(self)
            hbox.Add(panel, proportion=1, flag=wx.EXPAND)

            # 设置主窗口的布局为水平 BoxSizer
            self.SetSizer(hbox)

            self.Show()


    app = wx.App()
    MyFrame(None, "Vertical Buttons")
    app.MainLoop()
