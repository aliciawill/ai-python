from django.contrib import admin
from django.urls import path

import member.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.start),
    path('member/', member.views.index),
    path('member/insert', member.views.insert),
    path('member/insert2', member.views.insert2),
    path('member/del', member.views.delete),
    path('member/del2', member.views.delete2),
]
