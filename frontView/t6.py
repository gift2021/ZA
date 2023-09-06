if __name__ == '__main__':
    import tkinter as tk
    from tkinter import scrolledtext
    import subprocess

    # 创建主窗口
    root = tk.Tk()
    root.title("Python Editor")

    # 创建文本编辑器控件
    editor = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    editor.pack(fill=tk.BOTH, expand=True)


    # 创建运行按钮
    def run_python_code():
        code = editor.get("1.0", tk.END)
        try:
            # 使用 subprocess 运行 Python 代码
            result = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT, universal_newlines=True)
            output.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            output.insert(tk.END, e.output)


    run_button = tk.Button(root, text="Run", command=run_python_code)
    run_button.pack()

    # 创建输出窗口
    output = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    output.pack(fill=tk.BOTH, expand=True)

    # 启动主循环
    root.mainloop()
