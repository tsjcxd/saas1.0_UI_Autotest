'''
coding=utf-8
Tina 2018-08-22
添加门店/场地
脚本执行频率：较低
'''

import time
from appModules.add_store import AddStore
from parameterized.parameterized import parameterized
from appModules.delete_store import DeleteStore
from appModules.add_site import AddSite
from testScripts.test_login import Login
import unittest
from util.check_data import CheckData





class Setting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        print("添加门店及场地以及门店的删除")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




    # 添加门店
    def test01_add_store(self):
        AddStore.add_store(self.driver,'懒猫馆——自动化测试数据不能删除','14565456674','310000','310000','310104','徐汇区田林路100号')
        CheckData.check_data(self.driver,'//table[@class="table-1 edit-mode"]','懒猫馆——测试数据不能删除',2)
        time.sleep(3)

    # 添加场地
    def test02_add_site(self):
        AddSite.add_site(self.driver)

    # 删除门店
    def test03_delete_store(self):
        DeleteStore.deletestore(self.driver)








if __name__ == '__main__':
    unittest.main()