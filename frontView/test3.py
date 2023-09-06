if __name__ == '__main__':
    import wx


    class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

            # 创建一个左侧的树形控件（菜单栏）
            tree = wx.TreeCtrl(self, style=wx.TR_DEFAULT_STYLE)

            # 添加根节点
            root = tree.AddRoot("菜单")

            # 添加子节点表示不同的菜单选项
            file_node = tree.AppendItem(root, "文件")
            edit_node = tree.AppendItem(root, "编辑")
            view_node = tree.AppendItem(root, "视图")

            # 在文件菜单下添加子菜单选项
            tree.AppendItem(file_node, "打开")
            tree.AppendItem(file_node, "保存")
            tree.AppendItem(file_node, "退出")

            # 在编辑菜单下添加子菜单选项
            tree.AppendItem(edit_node, "复制")
            tree.AppendItem(edit_node, "粘贴")
            tree.AppendItem(edit_node, "剪切")

            # 在视图菜单下添加子菜单选项
            tree.AppendItem(view_node, "全屏")
            tree.AppendItem(view_node, "缩放")

            # 设置树形控件的根节点为当前活动节点
            tree.Expand(root)

            # 创建一个主布局，将树形控件添加到左侧
            main_sizer = wx.BoxSizer(wx.HORIZONTAL)
            main_sizer.Add(tree, proportion=1, flag=wx.EXPAND)

            # 创建右侧的面板，用于显示菜单选项内容
            panel = wx.Panel(self)
            main_sizer.Add(panel, proportion=2, flag=wx.EXPAND)

            self.SetSizer(main_sizer)
            self.Show()


    app = wx.App()
    MyFrame(None, "左侧菜单栏示例")
    app.MainLoop()
