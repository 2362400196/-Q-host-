import hashlib
from myadmin.models import User_zhuce3
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from myadmin.models import *
@csrf_exempt
def login(request):
    uname = request.POST.get("username",None)
    upass = request.POST.get("password",None)
    m = hashlib.md5()
    m.update(upass.encode(encoding='utf-8'))
    pwdd=m.hexdigest()
    mod=User_zhuce3.objects.filter(username=uname)
    for use in mod:
        p=use.password
        s=use.state
    print(p,pwdd,s)
    if pwdd==p and s=='1':
        #登录成功,将当前地登录成功的会员信息放置到session中
        request.session['idc_user'] = {'username':uname,'password':upass}
        return redirect(reverse('usermain'))

    elif pwdd==p and s=='0':
        context = {'errorinfo':"检测账号未激活，请前去邮箱激活！"}
        return render(request,'myapp/login.html',context)
    else:
        #登录失败
        context = {'errorinfo':"登录账号或密码错误！"}
        return render(request,'myapp/login.html',context)
#执行用户退出
def doLogout2(request):
    del request.session['idc_user'] #删除session信息
    return redirect(reverse('usermain')) 
