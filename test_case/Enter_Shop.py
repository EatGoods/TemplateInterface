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
EnterShop = readExcel.ReadExcel().get_xls("EnterShop.xlsx","shop")
url = readConfig.ReadConfig().get_http("baseurl")
@paramunittest.parametrized(*EnterShop)
class testEnterShop(unittest.TestCase):
    def setParameters(self,case_name,path,data,method):
        self.case_name = case_name
        self.path = path
        self.data = data
        self.method = method

    def description(self):
        self.case_name

    def setUp(self):
        print("测试开始")

    def testGetEnterShop(self):
        self.GetEnterShop()

    def tearDown(self):
        print("测试结束")

    def GetEnterShop(self):
        info = RunMain().run_main(self.method,url+self.path,self.data)
        print(info)
        res = json.loads(info)
        self.assertEquals(res["code"],200)
