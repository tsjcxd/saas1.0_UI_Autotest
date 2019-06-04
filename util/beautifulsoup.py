# from selenium import webdriver
# from driver.get_driver import *
# from driver.get_url import *
# from appModules.LoginAction import LoginAction
from appModules.store_card_setting import StoreCardSetting
from util.Parameterize import parameterize
import unittest
from testScripts.test_login import Login
#


driver=Login.test_login()
# class jicheng(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.parame = parameterize()
#         cls.cardname = cls.parame.get_params("储值卡自动化")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    # def test01_login(self):
    #     self.driver.get(url)
    #     self.driver.maximize_window()
    #     LoginAction.login(self.driver,username,password)

class AddCard(unittest.TestCase):
    @staticmethod
    def test02_AddCard():
        parame = parameterize()
        cardname = parame.get_params("储值卡自动化")
        StoreCardSetting.CardSetting(driver,cardname)