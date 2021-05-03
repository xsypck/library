"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from login import views

#在浏览器输入路径，找到这里，指向view中的函数
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.index),#path(route, view, kwargs=None, name=None)
    path('calpage/',views.calpage),#不是调用函数，只是指给它
    path('cal',views.cal),
    path('list',views.callist),
    path('clean',views.clean),
    path('home/',views.home)
]
