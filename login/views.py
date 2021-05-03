from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models
# Create your views here.
def index(request):#前端发过来的都是请求
    return render(request,'login.html')#返回一个渲染页面

def calpage(request):
    return render(request,'cal.html')

def cal(request):
    if request.POST:
        valuea=request.POST['value1']
        valueb=request.POST['value2']#得到的都是字符串
        result=int(valuea)+int(valueb)
        models.cal.objects.create(valuea=valuea,valueb=valueb,result=result)
        return render(request,'result.html',context={'data':result})#递交网页
    else:
        return HttpResponse('please enter by post!')

def callist(request):
    data=models.cal.objects.all()
    return render(request,'list.html',context={'data':data})

def clean(request):
    models.cal.objects.all().delete()
    return HttpResponse('OKK!')#返回字符串

def home(request):
    return render(request,'home.html')