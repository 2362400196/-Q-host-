#逻辑处理
from myadmin.bt_host import bt_api
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from myadmin.models import Kangle_server
from myadmin.models import *
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
#kangle服务器添加处理
def kangle_server_logic(request):
    server_ip = request.POST.get("server_ip")
    server_name = request.POST.get("server_name")
    server_pwd = request.POST.get("server_pwd")
    server_key = request.POST.get("server_key")
    server_type = request.POST.get("server_type")
    end_time = request.POST.get("end_time")
    # 进行校验
    if server_ip != "" and server_name != "1":
        # ajx请求返回的就是json数据,不能返回页面或重定向
        mod=Kangle_server.objects.create(server_ip=server_ip,server_name=server_name,
        server_pwd=server_pwd,server_key=server_key,server_type=server_type,end_time=end_time)
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})
    
    

def deal_ajax(request):
    
    u = request.POST.get("username")
    p = request.POST.get("password")
    print(u)
    # 进行校验
    if u == "1" and p == "1":
        # 用户名和密码正确
        # ajx请求返回的就是json数据,不能返回页面或重定向
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})


#bt_host配置页面
def bt_host_api(request):
    ip = request.POST.get("ip",None)
    name = request.POST.get("name",None)
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)
    key = request.POST.get("key",None)
    

    # 进行校验
    if ip != "" and username != "" and password !=''and key !='':
        
        # ajx请求返回的就是json数据,不能返回页面或重定向
        mod=bt_host.objects.create(ip=ip,name=name,username=username,password=password,key=key,state='0')
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})

#bt_host添加主机
def bt_host_add_api(request):
    example = request.POST.get("example",None)
    bt_name = request.POST.get("bt_name",None)
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)
    key = request.POST.get("key",None)
    mod=bt_host_user.objects.filter(associated=example)
    p=''
    for use in mod:
        p=use.associated
        print(p)
   
    if p=='':
        print(bt_name)
        id=bt_api('http://23.224.81.243/api/vhost/user_create?')
        
    else:
        print(p)
    
    # 进行校验
    if example != "" and username != "" and password !=''and key !='':
        
        # ajx请求返回的就是json数据,不能返回页面或重定向
        
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})

#dns配置
def dns_config_1(request):
    name = request.POST.get("name",None)
    dns = request.POST.get("dns",None)
    dns_config.objects.create(name=name,dns=dns)
    print(dns)
    
    # 进行校验
    if dns!='':
        
        # ajx请求返回的就是json数据,不能返回页面或重定向
        
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})

#dns配置SecretId
def dns_configuration_1(request):
    name1 = request.POST.get("name1",None)
    SecretId = request.POST.get("SecretId",None)
    SecretKey = request.POST.get("SecretKey",None)
    ob=dns_configuration.objects.filter()
    if ob.count() == 0:
        dns_configuration.objects.create(name=name1,SecretId=SecretId,SecretKey=SecretKey)
    else:
        dns_configuration.objects.filter(id=1).update(name=name1,SecretId=SecretId,SecretKey=SecretKey)
    print(name1)
    
    # 进行校验
    if SecretId!=''and SecretKey!='':
        
        # ajx请求返回的就是json数据,不能返回页面或重定向
        
        return JsonResponse({"res": 1})
    else:
        # 用户名和密码错误
        return JsonResponse({"res": 0})


def dns_jiexi_a(request):
    name = request.POST.get("name",None)
    dns = request.POST.get("dns",None)
    dns_zhi = request.POST.get("dns_zhi",None)
    dns_jiexi = request.POST.get("dns_jiexi",None)
    dns_time = request.POST.get("dns_time",None)
    username = request.POST.get("username",None)
    ob=dns_configuration.objects.all()
    
    for i in ob:
        SecretId=i.SecretId
        SecretKey=i.SecretKey
   
    try: 
        cred = credential.Credential(SecretId, SecretKey) #这里需要自己获取，获取方法官方有教程
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = dnspod_client.DnspodClient(cred, "", clientProfile) 

        req = models.CreateRecordRequest()
        params = {
            "Domain": dns,#域名选择
            "SubDomain": dns_zhi,#主机记录
            "RecordType": "A",
            "RecordLine": "默认",
            "Value": dns_jiexi
            #23.224.81.243
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateRecord(req) 
        print(resp.to_json_string())
        dns_save.objects.create(name=name,user=username,dns_zhi=dns_zhi,dns=dns,dns_jie=dns_jiexi,endtime=dns_time) 
        return JsonResponse({"res": 1})

    except TencentCloudSDKException as err: 
        print(err) 
        return JsonResponse({"res": 0})
    
   
        

    