from django.contrib import admin
from django.urls import path

import member.views
## import할때는 py파일까지 해주세요!!

##urls.py에는 주소하나당 함수하나를 연결
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.index),
    path('member/', member.views.start),
    path('member/index1', member.views.index1),
    path('member/index2', member.views.index2),
    path('member/index3', member.views.index3),
]
