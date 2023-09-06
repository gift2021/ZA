if __name__ == '__main__':
    import wx


    class LeftMenuPanel(wx.Panel):
        def __init__(self, parent):
            super(LeftMenuPanel, self).__init__(parent)

            # 创建一个垂直的 BoxSizer，用于容纳菜单项
            vbox = wx.BoxSizer(wx.VERTICAL)

            # 添加菜单项到垂直 BoxSizer 中
            button1 = wx.Button(self, label='Menu Item 1')
            button2 = wx.Button(self, label='Menu Item 2')
            button3 = wx.Button(self, label='Menu Item 3')

            vbox.Add(button1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            vbox.Add(button2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            vbox.Add(button3, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

            # 设置容器离顶部和底部的间隔
            vbox.Add((-1, 10))  # 用于在顶部创建一些空白
            vbox.Add((-1, 10))  # 用于在底部创建一些空白

            # 将垂直 BoxSizer 设置为当前 Panel 的布局
            self.SetSizer(vbox)


    class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

            # 创建左侧菜单栏
            left_menu = LeftMenuPanel(self)

            # 创建右侧的面板，用于显示菜单选项内容
            panel = wx.Panel(self)

            # 创建主布局，将左侧菜单栏和右侧面板添加到水平 BoxSizer 中
            main_sizer = wx.BoxSizer(wx.HORIZONTAL)
            main_sizer.Add(left_menu, proportion=1, flag=wx.EXPAND)
            main_sizer.Add(panel, proportion=2, flag=wx.EXPAND)

            self.SetSizer(main_sizer)
            self.Show()


    app = wx.App()
    MyFrame(None, "Left Menu Example")
    app.MainLoop()
