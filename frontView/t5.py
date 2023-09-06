if __name__ == '__main__':
    import wx


    class MyMenuBar(wx.MenuBar):
        def __init__(self):
            super(MyMenuBar, self).__init__()

            # 创建一个 "File" 菜单
            file_menu = wx.Menu()
            file_menu.Append(wx.ID_OPEN, "Open")
            file_menu.Append(wx.ID_SAVE, "Save")
            file_menu.Append(wx.ID_EXIT, "Exit")

            # 创建一个 "Edit" 菜单
            edit_menu = wx.Menu()
            edit_menu.Append(wx.ID_COPY, "Copy")
            edit_menu.Append(wx.ID_CUT, "Cut")
            edit_menu.Append(wx.ID_PASTE, "Paste")

            # 将 "File" 菜单添加到菜单栏
            self.Append(file_menu, "File")

            # 将 "Edit" 菜单添加到菜单栏
            self.Append(edit_menu, "Edit")


    class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

            # 创建菜单栏对象
            menubar = MyMenuBar()

            # 将菜单栏添加到主窗口
            self.SetMenuBar(menubar)

            # 创建一个面板
            panel = wx.Panel(self)

            self.Show()


    app = wx.App()
    MyFrame(None, "Menu Bar Example")
    app.MainLoop()
