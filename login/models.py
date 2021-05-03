from django.db import models

#一张表就是一个class
#这只是表的一个表述部分，保存了，并没有启动数据库
#python manage.py makemigrations
class cal(models.Model):
    valuea=models.CharField(max_length=10)#valuea=models.CharField(max_length=10)长度为10的字符串
    valueb=models.CharField(max_length=10)
    result=models.CharField(max_length=10)