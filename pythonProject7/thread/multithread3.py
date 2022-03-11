import threading
import time
from tkinter import *

class RacingCar:
    #멤버변수
    name = ''

    #초기화함수
    def __init__(self, name):
        #self: 클래스로 생성한 객체!
        #c1 = RacingCar('appleCar')
        #self == c1
        #c1.name = 'appleCar'
        self.name = name
    #멤버함수
    def runCar(self):
        for _ in range(10):
            print(self.name + '~~달립니다.')

def run_start():
    # 라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!!')
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.

if __name__ == '__main__':
    window = Tk()
    window.geometry("500x250")
    window.title('멀티 스레드 자동차 경주')
    b = Button(window, text='멀티 스레드 시작',
               command=run_start)
    b.pack(side = TOP, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)
    car_label1 = Label(window, text='appleCar')
    car_label1.place(x = 10, y = 100)
    car_label2 = Label(window, text='summerCar')
    car_label2.place(x = 10, y = 150)
    car_label3 = Label(window, text='springCar')
    car_label3.place(x = 10, y = 200)
    window.mainloop()
