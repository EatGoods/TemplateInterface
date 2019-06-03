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
TemplateList = readExcel.ReadExcel().get_xls("TemplateList.xlsx","TemplateList")
url = readConfig.ReadConfig().get_http("baseurl")
@paramunittest.parametrized(*TemplateList)
class testTemplateList(unittest.TestCase):
    def setParameters(self,case_name,path,data,method):
        self.case_name = case_name
        self.path = path
        self.data = data
        self.method = method

    def description(self):
        self.case_name

    def setUp(self):
        print("测试开始")

    def testTemplateList(self):
        self.TemplateList()

    def tearDown(self):
        print("测试结束")

    def TemplateList(self):
        info = RunMain().run_main(self.method,url+self.path,self.data)
        print(info)
        res = json.loads(info)
        self.assertEquals(res["code"],200)