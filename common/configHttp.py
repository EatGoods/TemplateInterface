import requests
import json
session = requests.Session()
class RunMain():
    def getSession(self):
        login_url = "https://api.wsc.t5128.com/admin/login/login"
        data = {"business_username":"17371177785","business_password":"qwer123456"}
        r = session.post(login_url,data)
        print(r.cookies)
        return session

    def send_Post(self,url,data):
        result = session.post(url= url,data= data).json()
        res = json.dumps(result ,ensure_ascii= False , sort_keys= True , indent= 2)
        return  res

    def send_Get(self,url,data):

        result = session.get(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self,method ,url = None ,data = None):
        self.getSession()
        result = None
        if method == 'post' or method =='POST':
            result = self.send_Post(url,data)
        elif method == 'get' or method =='GET':
            result = self.send_Get(url,data)
        else:
            print("method值错误")
        return  result
