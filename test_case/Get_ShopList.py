import json
import paramunittest
import write.WriteExcel as WriteExcel
from common.configHttp import RunMain
import unittest
import read.readConfig as readConfig
import read.readExcel as readExcel
import getPath

book = WriteExcel.writeExcel()
basepath = getPath.get_basepath()
GetShopList = readExcel.ReadExcel().get_xls("GetShopList.xlsx","shoplist")
url = readConfig.ReadConfig().get_http("baseurl")
@paramunittest.parametrized(*GetShopList)
class testGetShopList(unittest.TestCase):
    def setParameters(self,case_name,path,data,method):
        self.case_name = case_name
        self.path = path
        self.data = data
        self.method = method

    def description(self):
        self.case_name

    def setUp(self):
        print("测试开始")

    def testGetShopList(self):
        self.GetShopList()

    def tearDown(self):
        print("测试结束")

    def GetShopList(self):
        info = RunMain().run_main(self.method,url+self.path,self.data)
        print(info)
        res = json.loads(info)
        self.assertEquals(res["code"], 200)
        shop_id = res["data"]["list"][0]["shop_id"]
        print(shop_id)
        data = "/admin/shop/shop/checkshop?shop_id="+str(shop_id)
        book.write_excel("shop","EnterShop",data,None,"get","EnterShop.xlsx")
