from tkinter import *

def save():
    pass
def read():
    pass

window = Tk()
window.geometry('500x600')
icon = PhotoImage(file='r7.png')
top = Label(window, image=icon)
top.pack()

id_label = Label(window, text='ID입력')
id_label.pack()
id_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
id_entry.pack()
name_label = Label(window, text='NAME입력')
name_label.pack()
name_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
name_entry.pack()
url_label = Label(window, text='URL입력')
url_label.pack()
url_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
url_entry.pack()
img_label = Label(window, text='IMG입력')
img_label.pack()
img_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
img_entry.pack()
save = Button(window, width=30, height=3,
              bg='green',
              font=('애플 고딕', 20),
              text='DB에 저장',
              command=save
              )
save.pack()
read = Button(window, width=30, height=3,
              bg='green',
              font=('애플 고딕', 20),
              text='DB에서 읽기',
              command=read
              )
read.pack()
window.mainloop()
