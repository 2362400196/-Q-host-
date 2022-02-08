
import yagmail
import string 
import random
import hashlib
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from myadmin import models
from myadmin.models import User_zhuce3,bt_host_user
from email.mime.text import MIMEText
from email.header import Header
from myadmin.bt_host import bt_api
#发送邮件模块
def  smtp(emain,con):
    # 连接邮箱服务器
    yag = yagmail.SMTP(user="2362400196@qq.com",password="mgyfyvksqdgydhha",host="smtp.qq.com")
    # 邮箱正文
    contents = [con]

    yag.send([emain],'注册激活',contents)
#注册验证模块
@csrf_exempt
def add(request):
    s = string.ascii_letters
    s1 = string.ascii_letters
    s2 = string.ascii_letters
    s3 = string.ascii_letters
    r = random.choice(s)
    r1 = random.choice(s1)
    r2 = random.choice(s2)
    r3 = random.choice(s3)
    username= request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    mod=User_zhuce3.objects.filter(username=username)
    mod2=User_zhuce3.objects.filter(email=email)
    p=''
    e=''
    for use in mod:
        p=use.username
    for use2 in mod2:
        e=use2.email
    pw=r+r1+r2+r3
    m = hashlib.md5()
    m.update(pw.encode(encoding='utf-8'))
    pwdd=m.hexdigest()
    m1 = hashlib.md5()
    m1.update(password.encode(encoding='utf-8'))
    pwdd1=m1.hexdigest()
    print('用户名',p,'邮箱',e)
    # 进行校验
    if username=='' or password=='' or email=='':
        # 错误
        return JsonResponse({"res": 0})
    elif p ==''and e=='':

        #
        models.User_zhuce3.objects.create(username=username,password=pwdd1,email=email,state='0',pw=pwdd,yue='0')
        
        
        #models.bt_host_user.objects.create(username=username,password=pwdd1,associated=id)

        
        con="<a href='www.baidu.com'><h1>点击链接，激活你的账号吧</h1></a>http://idc.qingningz.cn/email_validation?pwd=%s"%(pwdd)
        smtp(email,con)
        print('创建成功')
        return JsonResponse({"res": 1})
    elif username==p or email==e:
        print('用户名不对',p)
        return JsonResponse({"res": 2}) 

    

#邮箱验证函数
def email_validation(request):
    a=request.GET['pwd']
    mod=User_zhuce3.objects.filter(pw=a)
    for use in mod:
        p=use.pw

    if p==a:
        mod1=User_zhuce3.objects.filter(pw=a)
        for use1 in mod1:
            p1=use1.id
            print(p1)
        step = User_zhuce3.objects.get(id=p1)

        step.state = '1'

        step.save()
        return HttpResponse('<script>alert("激活成功，请登录");location.href="/login";</script>')
    else:
        return HttpResponse('<script>alert("激活失败了，请重新激活");location.href="/login";</script>')
    
