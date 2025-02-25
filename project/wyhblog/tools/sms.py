import datetime
import hashlib
import base64
import json

import requests  #发http/https请求

class YunTongxin():

    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):

        self.accountSid = accountSid#账户id
        self.accountToken = accountToken#授权令牌
        self.appId = appId#应用id
        self.templateId = templateId#模板id

    def get_request_url(self, sig):
        #/2013-12-26/Accounts/{accountSid}/SMS/{funcdes}?sig={SigParameter}
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s'%(self.accountSid, sig)
        return self.url

    def get_timestamp(self):
        #生产时间戳
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def get_sig(self, timestamp):
        #生产业务url中的sig
        s = self.accountSid + self.accountToken + timestamp
        m = hashlib.md5()
        m.update(s.encode())
        return m.hexdigest().upper()

    def get_request_header(self, timestamp):
        #生产请求头
        s = self.accountSid + ':' + timestamp
        auth = base64.b64encode(s.encode()).decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': auth
        }

    def get_request_body(self, phone, code):

        return {
            "to": phone,
            "appId": self.appId,
            'templateId': self.templateId,
            'datas': [code, "3"]
        }

    def request_api(self, url, header, body):
        res = requests.post(url, headers=header, data=body)
        return res.text

    def run(self, phone, code):
        #获取时间戳
        timestamp = self.get_timestamp()
        #生产签名
        sig = self.get_sig(timestamp)
        #生产业务url
        url = self.get_request_url(sig)
        # print(url)
        headers = self.get_request_header(timestamp)
        # print(headers)
        #生产请求体
        body = self.get_request_body(phone, code)
        #发请求
        data = self.request_api(url, headers, json.dumps(body))
        return data

if __name__ == '__main__':

    #accountSid, accountToken, appId, templateId
    config = {
        "accountSid": "2c94811c9035ff9f0192b2cb0f377eef",
        "accountToken": "54684925351045bd858a411d62899eb5",
        "appId": "2c94811c9035ff9f0192b2cb10e87ef6",
        "templateId": "1"
    }

    yun = YunTongxin(**config)
    res = yun.run("15960373346", "1234")
    print(res)