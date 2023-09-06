import wx

class MyFrame(wx.Frame):

    def __init__(self,parent,title):
        super(MyFrame, self).__init__(parent,title=title,size=(600,800))
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT,'Quit','Quit application')
        menubar.Append(fileMenu,'&file')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)

        # self.SetSize(300,200)
        self.Centre()

        # 创建左侧菜单栏
        left_menu = LeftMenuPanel(self)

        # 创建右侧的面板，用于显示菜单选项内容
        panel = wx.Panel(self)
        # 创建主布局，将左侧菜单栏和右侧面板添加到水平 BoxSizer 中
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(left_menu, proportion=0, flag=wx.EXPAND)  # 使用 proportion 控制左侧菜单栏的大小
        main_sizer.Add(panel, proportion=1, flag=wx.EXPAND)

        self.SetSizer(main_sizer)
        self.Show()

    def OnQuit(self,e):
        self.Close()

class LeftMenuPanel(wx.Panel):
    def __init__(self,parent):
        super(LeftMenuPanel, self).__init__(parent)

        # 设置左侧菜单栏的背景颜色为蓝色
        # self.SetBackgroundColour(wx.Colour(0, 0, 255))  # 设置为蓝色，可以根据需要修改颜色

        # 创建一个垂直的 BoxSizer，用于容纳菜单项
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加菜单项到垂直 BoxSizer 中
        button1 = wx.Button(self, label='行情数据')
        button2 = wx.Button(self, label='回测结果')
        button3 = wx.Button(self, label='策略编写')

        vbox.Add(button1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(button3, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 设置容器离顶部和底部的间隔
        vbox.Add((-1, 10))  # 用于在顶部创建一些空白
        vbox.Add((-1, 500))  # 用于在底部创建一些空白

        vbox.Add((-1, 10))

        # 将垂直 BoxSizer 设置为当前 Panel 的布局
        self.SetSizer(vbox)


def main():
    app = wx.App()
    ex = MyFrame(None,"ZA")
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()