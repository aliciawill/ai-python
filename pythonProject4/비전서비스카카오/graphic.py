from tkinter import *
from tkinter import messagebox
#import tkinter

#버튼을 눌렀을 때 로그인 기능을 처리해야함.
#특정한 기능은 하나의 함수로 만들어 주면 됨.
#버튼 눌렀을 때 처리하고자 하는 기능하나는 함수하나가 됨.
#함수를 만드는 것을 함수를 정의한다라고 함.
#기능을 프로그래머가 정의하기 때문에 함수를 정의한다라고 표현함.
def login():
    #id입력한 값, pw입력한 값 가지고 와야함.
    #원래 회원가입할 때의 id/pw와 입력한 값을 비교해야함.
    id2 = id_entry.get() #root
    print('입력한 id는 ', id2)
    pw2 = pw_entry.get() #root
    print('입력한 pw는 ', pw2)
    #pw 입력한 값 가지고와서 프린트
    #원래의  id:root/pw:1234
    #원래의 id/pw와 입력한 id/pw가 동일한지 판별하여 프린트
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인 성공', '축하합니다.')
        print('로그인 성공')
    else:
        messagebox.showinfo('로그인 실패', '다시해보세요..')
        print('로그인 실패')

w = Tk()
w.geometry("500x250")

id = Label(w, text='ID입력', font=('궁서', 30)) #id글자
id.pack()

id_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white') #id입력
id_entry.pack()

pw = Label(w, text='PW입력' , font=('궁서', 30)) #pw글자
pw.pack()

pw_entry = Entry(w, font=('궁서', 30), bg='blue', fg='white') #pw입력
pw_entry.pack()

b = Button(w,
           text='로그인 처리',
           font=('궁서', 30),
           bg='yellow',
           command=login
           ) #클릭버튼
b.pack()



w.mainloop()