#This program can run better in Python 3
#Text to Unicode.py
#If you find any translation problems, please report
#English is translated by computer(Chinese -> English)

from tkinter import *

def Command():
    Output_Box.delete(0, END)
    for i in range(len(Input_Box.get())):
        Output_Box.insert((0 + len(Output_Box.get()) + 1), ("\\u" + (4 - len(hex(ord(Input_Box.get()[i])).upper()[2:])) * "0" + hex(ord(Input_Box.get()[i])).upper()[2:]))

TK_SILENCE_DEPRECATION = 1
TexttoUnicode = Tk()
Input_Box = Entry(TexttoUnicode, width = 30)
Input_Box.place(x = 50, y = 75)
Notice_Label = Label(TexttoUnicode, text = "Please enter the character you want to find Unicode encoding in the box below:") #Original: 请在下面的框中输入你想查找Unicode码位的字符:

Notice_Label.place(x = 50, y = 50)
Notice_Label2 = Label(TexttoUnicode, text = "Output(after click the Convert button):") #Original: 点击转换按钮后的输出:

Notice_Label2.place(x = 50, y = 125)
Output_Box = Entry(TexttoUnicode, width = 30)
Output_Box.place(x = 50, y = 150)
OK_Button = Button(TexttoUnicode, text = "Convert", command = Command) #Original: 转换
OK_Button.place(x = 400, y = 200)
TexttoUnicode.resizable(False, False)
TexttoUnicode.title("Text conversion Unicode encoding") #Original: 文字转换Unicode编码
TexttoUnicode.geometry("500x250")
TexttoUnicode.mainloop()
