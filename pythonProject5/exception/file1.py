## member.txt에 member정보를 3명 넣으세요.
## file2.py에서 member.txt를 읽어온 후
## 다음과 같이 출력되도록 해보세요.
## 이름       나이      연락처
## -----------------------
## hong     100         011
## park     150         019
## song     200         017

file = open('member.txt', 'a')

for _ in range(2):
    name = input('당신의 이름은 >> ')
    age = input('당신의 나이는 >> ')
    tel = input('당신의 연락처는 >> ')
    data = name + "," + age + "," + tel
    file.write(data)

file.close()

