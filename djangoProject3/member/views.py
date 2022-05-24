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