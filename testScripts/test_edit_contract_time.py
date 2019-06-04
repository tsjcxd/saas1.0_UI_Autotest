'''
coding=utf-8
Tina 2018-09-03
编辑储值卡合同的有效期
脚本执行频率：较低
'''
import unittest
from appModules.card_contract_expired import CardContractExpired
from appModules.private_contract_expired import PrivateContractExpired
from testScripts.test_login import Login


class TestEditCardContract(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        print("编辑储值卡合同和私教合同的有效期")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01_edit_card_contract(self):
        """编辑储值卡合同的有效期"""
        CardContractExpired.card_contract_expired(self.driver)

    def test02_edit_private_contract(self):
        """编辑私教合同的有效期"""
        PrivateContractExpired.private_contract_expired(self.driver)


if __name__ == '__main__':
    unittest.main()
