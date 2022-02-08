import hashlib
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from myadmin.models import Admin
@csrf_exempt
def login(request): 
    uname = request.POST.get("username",None)
    upass = request.POST.get("password",None)
    
    m = hashlib.md5()
    m.update(upass.encode(encoding='utf-8'))
    mod=Admin.objects#获取admin模型的操作对象
    uname_=mod.filter(user=uname)
    bb=''
    for pwd in uname_:
        bb=pwd.pwd 
        print(bb)
    
    if bb==m.hexdigest():
        #登录成功,将当前地登录成功的会员信息放置到session中
        request.session['diancan_user'] = {'username':uname,'password':upass}
        return redirect(reverse('index'))
    else:
        #登录失败
        context = {'errorinfo':"登录账号或密码错误！"}
        return render(request,'myadmin/login.html',context)
#执行用户退出
def doLogout(request):
    del request.session['diancan_user'] #删除session信息
    return redirect(reverse('index')) 
