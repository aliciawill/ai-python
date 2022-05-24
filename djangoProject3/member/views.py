from django.http import HttpResponse
from django.shortcuts import render, redirect
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


def up(req, id):
    #get(주소와 함께 전달되는 값은 컨트롤러의 함수안에
    #     같은 이름의 변수를 선언해주면 장고가 받아서 넣어준다.
    ##검색할 id를 받아와서
    print('전달받은 검색할 id는 ', id)
    ##db검색을 한후,
    one = Test.objects.get(id = id)
    print('db검색한 결과: ', one)
    context = {'one' : one}
    ##db검색한 결과를 context로 전달
    return render(req, 'member/up.html', context)

def up2(req):
    ##1. 전달되는 값 post방식으로 받고,
    data = req.POST
    ##2. id를 가지고 검색 후,
    one = Test.objects.get(id = data['id'])
    print('수정할 데이터 검색: ', one)
    ##3. update처리함.
    one.name = data['name']
    one.tel = data['tel']
    one.addr = data['addr']
    one.save()
    ##4. 결과를 알려줌.
    ##5. 검색을 해서 확인해보자.
    #return HttpResponse('수정 내용 확인하는 페이지')
    #urls.py에 있는 주소를 호출시에는 redirect를 써준다.
    return redirect('/member/one2/')





