#请求bthost  Api代码

import requests
import time
import random
import hashlib
import json

#创建bthost用户
def bt_api(url_): 
    t=int(time.time())
    r1=random.sample('ABCDEFGHJKMNPQRSTWXYZ',10)
    r=r1[0]+r1[1]+r1[2]+r1[3]+r1[4]+r1[5]+r1[6]+r1[7]+r1[8]#随机数
    print(r)
    token='Ygku1SjsUH'#密钥
    m=m=str(t)+str(r)+str(token)
    m1 = hashlib.md5()
    m1.update(m.encode(encoding='utf-8'))
    m2=m1.hexdigest().upper()  #签名
    url=url_+'time='+str(t)+'&random='+r+'&signature='+m2
    print(url)
    res=requests.get(url).text
    a=json.loads(res)
    actor=a['data']
    id=(actor['id'])
    print(id,a)
 

#bt_api('http://23.224.81.243/api/vhost/user_create?')


