import tkinter

window = tkinter.Tk()  # 实例化了一个窗口对象
window.title("计算器")  # 设置了窗口标题
window.geometry("477x831")  # 设置窗口大小

# 以下为各种组件
# 简而言之组件就是对象


# 增加一个标签对象 (标签组件)
lbl = tkinter.Label(window, text='hello', font=("Arial Bold", 50))
# 使用grid方法设置此标签对象在窗口对象中的位置
# lbl没有调用grid函数的话是不会显示的。
lbl.grid(column=0, row=0)


# 绑定按钮点击事件
def clicked():
    # lbl.configure(text='按钮被点击了!')
    lbl.insert(1,'1')



# 增加一个按钮对象  (按钮组件)
# 实例化一个按钮对象
btn = tkinter.Button(window, text="这是一个按钮",command = clicked)
btn.grid(column=1, row=0)

# 添加一个文本框
# 通过Tkinter的Entry类获取到用户输入。用Entry类创建一个文本框
# UserInput = tkinter.Entry(window, width=10)
# UserInput.grid(column=0, row=1)

# 进入消息循环,放在函数最后
window.mainloop()  # 这个函数将让窗口等待用户与之交互，直到我们关闭它。
# 若忘记调用mainloop函数的话，将不会向用户显示任何内容（没有窗口）。
