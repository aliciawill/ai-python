from functools import partial
from my_cal import *

cal = Cal()


def create_cal(op):
    print('op>> ', op)
    vvar1 = int(var1_entry.get())
    cal.numstr.append(vvar1)
    cal.numstr.append(op)
    var1_entry.delete(0, END)

    if (op == "-"):
        cal.minus(vvar1)
        print(cal.result)
    if (op == "+"):
        cal.plus(vvar1)
        print('-----')
        print(cal.result)
    if (op == "/"):
        cal.div(vvar1)
        print(cal.result)
    if (op == "*"):
        cal.multi(vvar1)
        print(cal.result)
    if (op == "="):
        # cal.result
        print('========')
        cal.plus(vvar1)
        print(cal.result)
        result_label.config(text=float(cal.result))
    if (op == "r"):
        cal.multi(n1=0)
        var1_entry.delete(0, END)
    print(cal)


# UI구성
w = Tk()
w.geometry("500x500")
var1 = Label(w, text='첫번째 수를 입력하세요', font=('궁서', 10))
var1_entry = Entry(w, font=('궁서', 10), bg='blue', fg='white')

plus = Button(w, text='+', font=('궁서', 10), bg='yellow', command=partial(create_cal, "+"))
minus = Button(w, text='-', font=('궁서', 10), bg='yellow', command=partial(create_cal, "-"))
multi = Button(w, text='x', font=('궁서', 10), bg='yellow', command=partial(create_cal, "*"))
div = Button(w, text='/', font=('궁서', 10), bg='yellow', command=partial(create_cal, "/"))
result = Button(w, text='=', font=('궁서', 10), bg='yellow', command=partial(create_cal, "="))
rs = Button(w, text='E', font=('궁서', 10), bg='yellow', command=partial(create_cal, "r"))
result_label = Label(w, text='result', font=('궁서', 10))

var1.pack()
var1_entry.pack()
plus.pack()
minus.pack()
multi.pack()
div.pack()
result.pack()
result_label.pack()
rs.pack()
w.mainloop()

