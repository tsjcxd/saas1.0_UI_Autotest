'''
coding=utf-8
User:Tina
Data:2018-08-22
添加潜在客户
脚本执行频率：低
'''


from appModules.add_potentital_customer import AddPotentitalCustomer
from appModules.formal_customer import FormalCustomer
from util.Parameterize import parameterize
import unittest
from testScripts.test_login import Login
from util.check_data import CheckData





class TestCustomer(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        params = parameterize()
        cls.customer = params.get_params("自动化——潜在客户")
        print("添加潜在客户")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




    # 添加潜在会员
    def test01_add_potentital_customer(self):
        """添加潜在会员以及验证添加是否成功"""
        AddPotentitalCustomer.add_potentital_customer(self.driver,self.customer)
        CheckData.check_data(self.driver,"//table[@class='table-1']",self.customer,5)



    # 潜在客户变成正式会员
    def test02_Add_Formal_Customer(self):
        """潜在会员变成正式会员以及验证入会是否成功"""
        FormalCustomer.formalCustomer(self.driver)
        CheckData.check_data(self.driver, "//table[@class='table-1']", self.customer,9)



if __name__ == '__main__':
    unittest.main()



