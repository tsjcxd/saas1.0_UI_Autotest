'''
coding=utf-8
User:Tina
Data：2018-08-23
会员购买私教合同
脚本执行频率：较高
'''

import time
from appModules.purchase_private_course import PurchasePrivateContract
from appModules.purchase_store_card import PurchaseCard
import unittest
from testScripts.test_login import Login
from util.check_data import CheckData
from util.opeartion_json import OperetionJson


class TestPurchaseContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        cls.opera_json = OperetionJson()
        print("会员购买储值卡和私教课程合同")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 正式会员“18321829313”购买私教合同：“私教课程测试不要删除”
    def test01_purchase_private_course(self):
        """购买私教合同以及验证购买是否成功"""
        PurchasePrivateContract.purchase_private_course(self.driver)
        privateCourseName = self.opera_json.get_data("test01_add_private_course")
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']",privateCourseName,7)
        time.sleep(2)

    def test02_purchase_store_card(self):
        """购买储值卡以及验证是否购买成功"""
        PurchaseCard.purchase_card(self.driver)
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']","储值卡不要删除数据",6)


if __name__ == '__main__':
    unittest.main()