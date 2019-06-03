import json
import paramunittest
from common.configHttp import RunMain
import unittest
import read.readConfig as readConfig
import read.readExcel as readExcel

getclass_xls = readExcel.ReadExcel().get_xls("getclass.xlsx","class")
url = readConfig.ReadConfig().get_http("baseurl")
@paramunittest.parametrized(*getclass_xls)
class testGetClass(unittest.TestCase):
    def setParameters(self,case_name,path,data,method):
        self.case_name = case_name
        self.path = path
        self.data = data
        self.method = method

    def description(self):
        self.case_name

    def setUp(self):
        print("测试开始")

    def testGetClass(self):
        self.getClass()

    def tearDown(self):
        print("测试结束")

    def getClass(self):
        info = RunMain().run_main(self.method,url+self.path,self.data)
        print(info)
        res = json.loads(info)
        self.assertEquals(res["code"], 200)
