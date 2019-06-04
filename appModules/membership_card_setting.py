'''
coding=utf-8
Tina 2018-08-22
添加会籍卡
'''

from pageObject.add_membership_card_object import AddMembershipCard
import time
from selenium.webdriver.support.ui import Select
class MembershipCardSetting:
    def __init__(self):
        print("")

    @staticmethod
    def membership_card_setting(driver,cardname):
        addshipcardsetting = AddMembershipCard(driver)
        driver.implicitly_wait(30)

        # 进入左侧的菜单：购买
        addshipcardsetting.go_purchase_menu_obj().click()

        # 切换至菜单：会籍卡设置
        addshipcardsetting.go_card_setting_obj().click()

        # 添加
        addshipcardsetting.add_card_obj().click()
        time.sleep(2)

        # 卡名称
        addshipcardsetting.name_obj().send_keys(cardname)

        # 卡类型
        Select(addshipcardsetting.card_type_obj()).select_by_value("3")

        # 有效天数
        addshipcardsetting.unit_obj().send_keys(1000)


        # 售卖基础价格
        addshipcardsetting.price_obj().send_keys(10)


        # 转让手续费
        addshipcardsetting.fee_obj().send_keys(1)

        # 可售卖门店
        addshipcardsetting.shop_select_obj().click()


        # 售卖时间
        addshipcardsetting.saletime_from_obj().send_keys("2018-10-17")
        addshipcardsetting.saletime_to_obj().send_keys("2019-12-17")
        time.sleep(2)

        # 可在线购买
        addshipcardsetting.purchase_obj().click()
        time.sleep(2)

        # 设置权重
        addshipcardsetting.weights_obj().send_keys(10)
        time.sleep(3)

        # 保存
        addshipcardsetting.confirm_obj().click()
        time.sleep(2)

        # 确认
        addshipcardsetting.confirm_button_obj().click()

        # 切换至菜单：会籍卡设置
        addshipcardsetting.go_card_setting_obj().click()

