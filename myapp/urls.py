#用户子路由配置
from myapp.views.index import index
from django.urls import path
from django.urls.resolvers import LocalePrefixPattern, URLPattern
from myapp.views import index
from myapp import Adduser
from myapp import Logical_processing

urlpatterns=[
    path('', index.index,name='index'),#主页
    path('login', index.login,name='login'),#网站登陆页
    path('usermain', index.main,name='usermain'),#网站框架页
    path('user', index.user,name='user'),#网站主页
    path('userregistered', index.registered,name='userregistered'),#注册
    path('user_pay', index.pay,name='user_pay'),#主页
    #-------------------------------------------------------
    #逻辑处理部分
    path('login_2', Logical_processing.login,name='login_2'),#网站登陆处理
    path('doLogout2', Logical_processing.doLogout2,name='doLogout2'),#网站首页

    path('adduser', Adduser.add,name='adduser'),#注册
    path('email_validation', Adduser.email_validation,name='email_validation'),#邮箱注册验证
]