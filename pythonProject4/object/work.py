class Worker:
    name = ''
    age = 0
    gender = ''
    count = 0 #직원수 누적
    age_sum = 0 #나이 누적
    m = 0 #성별누적
    f = 0 #성별누적
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Worker.count += 1
        Worker.age_sum += age
        if gender == '남':
            Worker.m += 1
        else:
            Worker.f += 1

    def __str__(self):
        return self.name + ' ' + \
               str(self.age) +  ' ' + \
               self.gender
