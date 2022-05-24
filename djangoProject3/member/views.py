from django.http import HttpResponse
from django.shortcuts import render

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
    return HttpResponse('회원 가입 처리 페이지')