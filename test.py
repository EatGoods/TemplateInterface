import requests
import json
session = requests.Session()
class Test:
    def getSession(self):
        login_url = "https://api.wsc.t5128.com/admin/login/login"
        data = {"business_username":"17371177785","business_password":"qwer123456"}
        r = session.post(login_url,data)
        print(r.cookies)
        return session
    def send_Get(self,url,data):
        result = session.get(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        print(res)


if __name__ == "__main__":
    Test().getSession();
    data = {
        "shop_id":128
    }
    Test().send_Get("https://api.wsc.t5128.com/admin/shop/shop/checkshop?shop_id=128",None)