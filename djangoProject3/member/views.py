from django.http import HttpResponse
from django.shortcuts import render
from member.models import Question, Test

# Create your views here.
def start(req):
    return HttpResponse('<center><h3>시작페이지</h3><hr color=red>' +
                        '<a href=/member/>회원정보 사이트</a><br>' +
                        '<a href=/question/>질문정보 사이트</a></center>'
                        )

def index(req):
    return render(req, 'member/index.html')

def insert(req):
    return render(req, 'member/insert.html')

def insert2(req):
    #1. 입력한 정보 받아서
    data = req.POST #dic
    print('서버에서 받은 데이터 >> ', data)
    print('name: ', data['name'])
    print('tel: ', data['tel'])
    print('addr: ', data['addr'])
    #2. db처리하고
    ##2-1.객체 생성
    one = Test(name=data['name'], tel=data['tel'], addr=data['addr'])
    ##2-2.save()
    one.save()
    #3. 결과를 알려주자.
    return render(req, 'member/insert2.html')

def delete(req):
    return render(req, 'member/delete.html')

def delete2(req):
    #1. 입력한 정보 받아서
    data = req.POST
    print(data)
    #2. db처리
    #2-1. 검색을 먼저하고
    one = Test.objects.get(id = data['id'])
    #one = Test.objects.filter(id = data['id'])
    print(one)
    #2-2. 지워주세요.
    one.delete()

    #3. 결과 알려줌.
    return render(req, 'member/delete2.html')

def one(req):
    return render(req, 'member/one.html')

def one2(req):
    data = req.POST
    idValue = data['id']
    one = Test.objects.get(id = idValue)
    print('db검색한 결과: ', one)
    result = {'one' : one,
              'test' : 100
              }
    #controller에서 template으로 값을 넘길때는
    #dictionary를 만들어 전달한다.
    return render(req, 'member/one2.html', context=result)
    # def render(request, templte, context):
    #     pass







