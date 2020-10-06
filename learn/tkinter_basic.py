import tkinter


def addLabel():
    global win, i
    wl = tkinter.Label(win, text="%d times!" % i, background="yellow")
    wl.pack()
    i += 1


win = tkinter.Tk()
win.geometry("600x400+150+100")
win.title("HELLO")
menuBar = tkinter.Menu(win)

fMenu = tkinter.Menu(menuBar)
for item in ["新建", "打开", "保存", "另存为", "退出"]:
    fMenu.add_command(label=item)

fMenu.add_command(label="保存", command=addLabel)

eMenu = tkinter.Menu(menuBar)
for item in ["复制", "粘贴", "剪切", "撤销"]:
    eMenu.add_command(label=item)

menuBar.add_cascade(label="⽂件", menu=fMenu)
menuBar.add_cascade(label="编辑", menu=eMenu)

win['menu'] = menuBar

i = 1

wl2 = tkinter.Label(win, text="HELLO WORLD", background="red", width=20)
wl2.pack(side="left", expand="no", fill="y")

b = tkinter.Button(win,
                   text="click",
                   command=addLabel,
                   background="green",
                   width=20)
b.pack(side="bottom")

win.mainloop()
