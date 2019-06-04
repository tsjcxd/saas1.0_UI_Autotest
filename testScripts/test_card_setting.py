'''
coding=utf-8
Tina 2018-08-22
添加会籍卡
脚本执行频率：较低
'''


from util.Parameterize import parameterize
from appModules.membership_card_setting import MembershipCardSetting
from appModules.store_card_setting import StoreCardSetting
from testScripts.test_login import Login
import unittest
from util.check_data import CheckData
from appModules.edit_membership_card import EditMembershipCard
from appModules.edit_store_card import EditStoreCard
from util.opeartion_json import OperetionJson


class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        cls.paras = parameterize()
        cls.paras = parameterize()
        cls.opera_json = OperetionJson()
        print("会籍卡和储值卡添加以及变成禁售")




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




    #添加会籍卡
    def test01_membership_card_setting(self):
        """添加会籍卡以及验证添加是否成功"""
        membership_card = self.paras.get_params("自动化测试会籍卡")
        MembershipCardSetting.membership_card_setting(self.driver,membership_card)
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']",membership_card,2)
        self.opera_json.check_json_value("test01_membership_card_setting",membership_card)


    #添加储值卡
    def test02_store_card_setting(self):
        """添加储值卡以及验证添加是否成功"""
        store_card = self.paras.get_params("自动化测试储值卡")
        StoreCardSetting.card_setting(self.driver,store_card)
        CheckData.check_data(self.driver,"//table[@class='table-1 edit-mode']",store_card,2)
        self.opera_json.check_json_value("test02_store_card_setting", store_card)

    # 会籍卡变为“禁售”
    def test03_edit_membership_card(self):
        """将会籍卡变为禁售，暂未验证"""
        cardname = self.opera_json.get_data("test01_membership_card_setting")  # 依赖用例 test01_membership_card_setting
        EditMembershipCard.edit_membership_card(self.driver,cardname)


    # 储值卡变为“禁售”
    def test04_edit_store_card(self):
        """将储值卡变为禁售，暂未验证"""
        cardname = self.opera_json.get_data("test02_store_card_setting")    # 依赖用例 test02_store_card_setting
        EditStoreCard.edit_store_card(self.driver,cardname)











