import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
def add():
    try: 
        cred = credential.Credential("AKIDBF8pS08irtyOVWl5Zr0xiGd4PdhabqFR", "85tZ3LRPCoKHRVN8h9VgfR1PbaR6lUei") #这里需要自己获取，获取方法官方有教程
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = dnspod_client.DnspodClient(cred, "", clientProfile) 

        req = models.CreateRecordRequest()
        params = {
            "Domain": "dzzxh.cn",#域名选择
            "SubDomain": "pay123",#主机记录
            "RecordType": "A",
            "RecordLine": "默认",
            "Value": "23.224.81.243"
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateRecord(req) 
        print(resp.to_json_string()) 

    except TencentCloudSDKException as err: 
        print(err) 


def deld():
    try:
        cred = credential.Credential("AKIDBF8pS08irtyOVWl5Zr0xiGd4PdhabqFR", "85tZ3LRPCoKHRVN8h9VgfR1PbaR6lUei") #这里需要自己获取，获取方法官方有教程
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        req = models.DeleteRecordRequest()
        params = {
            "Domain": "dzzxh.cn",
            "RecordId": 1049597560
        }
        req.from_json_string(json.dumps(params))

        resp = client.DeleteRecord(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        
        print(err)


#add()
deld()