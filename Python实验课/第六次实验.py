import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

t = tk.Text(window, height=1, font=("Arial Bold", 50), )  # 这里设置文本框高，可以容纳两行
t.pack()
# 这里的end表示插入在结尾，可以换为1.2，则插入在第一行第二位后面
b1 = tk.Button(window, text='1', width=5, height=2, command=lambda: t.insert('insert', '1')).pack(side='left')
b2 = tk.Button(window, text='2', width=5, height=2, command=lambda: t.insert('insert', '2')).pack(side='left')
b3 = tk.Button(window, text='3', width=5, height=2, command=lambda: t.insert('insert', '3')).pack(side='left')

b4 = tk.Button(window, text='4', width=5, height=2, command=lambda: t.insert('insert', '4')).pack(side='right')
b5 = tk.Button(window, text='5', width=5, height=2, command=lambda: t.insert('insert', '5')).pack(side='right')
b6 = tk.Button(window, text='6', width=5, height=2, command=lambda: t.insert('insert', '6')).pack(side='right')

b7 = tk.Button(window, text='7', width=5, height=2, command=lambda: t.insert('insert', '7')).pack(side='left')
b8 = tk.Button(window, text='8', width=5, height=2, command=lambda: t.insert('insert', '8')).pack(side='left')
b9 = tk.Button(window, text='9', width=5, height=2, command=lambda: t.insert('insert', '9')).pack(side='left')

window.mainloop()
