from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('测试组python毕业题')

img = Image.open('D:/Github/python/learn/1.jpg')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = Label(root, image=photo)
imglabel.grid(row=0, column=0, columnspan=3)

Label(root, text="Answer:").grid(row=1, column=0, sticky=S + N)

answerEntry = Entry(root)
btn = Button(root, text="Submit", command='submit')

answerEntry.grid(row=1, column=1)
btn.grid(row=1, column=2)

mainloop()
