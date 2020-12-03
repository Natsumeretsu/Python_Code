import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('600x500')

t = tk.Text(window, height=1, font=("Arial Bold", 50),)  # 这里设置文本框高，可以容纳两行
t.pack()

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame1.pack(padx=1, pady=1)
frame2.pack(padx=10, pady=10)
frame3.pack(padx=10, pady=10)

# 这里的end表示插入在结尾，可以换为1.2，则插入在第一行第二位后面
label = tk.Label(window, text="Label").pack
b1 = tk.Button(frame1, text='1', width=10, height=5, command=lambda: t.insert('insert', '1')).pack(side='left')
b2 = tk.Button(frame1, text='2', width=10, height=5, command=lambda: t.insert('insert', '2')).pack(side='left')
b3 = tk.Button(frame1, text='3', width=10, height=5, command=lambda: t.insert('insert', '3')).pack(side='left')

b4 = tk.Button(frame2, text='4', width=10, height=5, command=lambda: t.insert('insert', '4')).pack(side='left')
b5 = tk.Button(frame2, text='5', width=10, height=5, command=lambda: t.insert('insert', '5')).pack(side='left')
b6 = tk.Button(frame2, text='6', width=10, height=5, command=lambda: t.insert('insert', '6')).pack(side='left')

b7 = tk.Button(frame3, text='7', width=10, height=5, command=lambda: t.insert('insert', '7')).pack(side='left')
b8 = tk.Button(frame3, text='8', width=10, height=5, command=lambda: t.insert('insert', '8')).pack(side='left')
b9 = tk.Button(frame3, text='9', width=10, height=5, command=lambda: t.insert('insert', '9')).pack(side='left')


window.mainloop()
