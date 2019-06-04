'''
coding=utf-8
User:Tina
data:2018-08-22
添加员工（会籍销售/教练）
脚本执行频率：较低
'''

import time
from appModules.add_sales import AddSales
from appModules.add_coach import AddCoach
import unittest
from util.Parameterize import parameterize
from testScripts.test_login import Login
from util.check_data import CheckData
from appModules.delete_staff import DeleteStaff
from util.opeartion_json import OperetionJson





class TestAddStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        cls.paras = parameterize()
        cls.opera_json = OperetionJson()
        print("新增会籍销售和教练以及验证是否成功")
        print("删除会籍销售和教练，暂未验证")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    # 添加员工——会籍销售
    def test01_add_membership_sales(self):
        """添加会籍销售以及验证添加是否成功"""
        sales = self.paras.get_params("会籍销售自动化测试")
        AddSales.add_salse(self.driver, sales)
        self.opera_json.check_json_value("test01_add_membership_sales", sales)
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']",sales,6)



    # 添加员工——教练（私教教练/团课教练）
    def test02_add_coach(self):
        """添加教练以及验证添加是否成功"""
        paras = parameterize()
        coach = paras.get_params("教练自动化测试")
        AddCoach.add_coach(self.driver,coach)
        self.opera_json.check_json_value("test02_add_coach", coach)
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']",coach,6)
        time.sleep(3)

    # 删除员工——会籍销售
    def test03_delete_sales(self):
        """删除员工——会籍销售，暂未验证"""
        sales = self.opera_json.get_data("test01_add_membership_sales")      # 依赖用例 test01_add_membership_sales
        DeleteStaff.delete_staff(self.driver,sales)

    # 删除员工——教练
    def test04_delete_coach(self):
        """删除员工——教练，暂未验证"""
        coach = self.opera_json.get_data("test02_add_coach")      # 依赖用例 test02_add_coach
        DeleteStaff.delete_staff(self.driver,coach)




if __name__ == '__main__':
    unittest.main()