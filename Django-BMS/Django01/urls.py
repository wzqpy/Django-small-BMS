"""Django02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

# 导入 视图下面的函数
from home01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.oneviews),
    path('add/', views.addbook),
    path('look/', views.lookbook),
    re_path('books/(\d+)/edit/$', views.editbook),
    re_path('books/(\d+)/delete/$', views.deletebook),
    re_path('books/(\d+)/aut_more/$', views.aut_more),
    re_path('books/(\d+)/pub_more/$', views.pub_more),

    #(\d+) 正则匹配
]