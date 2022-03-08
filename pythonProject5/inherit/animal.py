class Animal:
    name = ''

    def __init__(self, name):
        self.name = name
    #self => 생성된 객체(주소)
    #a1 = Animal('hong')
    #a1.name = 'hong'

    #기능(객체가 생성된 후 호출이 가능)
    #객체가 생성되면 주소가 생김.
    #주소가 있어야 함수호출이 가능하다.
    #객체가 생성이 되고, 주소가 있어야
    #이 기능을 쓸 수 있다.(함수호출을 할 수 있다.)
    #a1.move()
    def move(self):
        print('move!!')
    def speak(self):
        pass