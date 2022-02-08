#用户前台视图
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from myadmin.models import User_zhuce3
# Create your views here.
#网站首页
def index(request):
    
    return render(request,'myapp/index.html')

#用户登陆页面
def login(request):
    return render(request,'myapp/login.html')
    #用户注册页面
def registered(request):
    return render(request,'myapp/registered.html')
#用户页面
def main(request):
    return render(request,'myapp/main.html')

#用户主页面
def user(request):
    a=request.session.get('idc_user')
    username=(a['username'])
    mod=User_zhuce3.objects.filter(username=username)
    for use in mod:
        yue=use.yue
        money=[yue]
        print(money)
    return render(request,'myapp/user.html',{'money':money})
#用户充值页面
def pay(request):
    return render(request,'myapp/pay.html')


 

