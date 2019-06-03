import os
import getPath
from xlwt import Workbook

basepath = getPath.get_basepath()
class writeExcel():
    def write_excel(self,sheet,case_name,path,data,method,name):
        book = Workbook(encoding="utf-8")
        sheet1 = book.add_sheet(sheet)
        sheet1.write(0, 0, "case_name")
        sheet1.write(0, 1, "path")
        sheet1.write(0,2,"data")
        sheet1.write(0, 3, "method")
        sheet1.write(1, 0, case_name)
        sheet1.write(1, 1, path)
        sheet1.write(1, 2, data)
        sheet1.write(1, 3, method)
        path = os.path.join(basepath,"test_file\case",name)
        print(os.path.exists(path))
        if os.path.exists(path):
            os.remove(path)
        book.save(path)
