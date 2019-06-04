'''
coding=utf-8
Tina 2018-09-03
编辑储值卡合同的有效期
'''

from pageObject.card_contract_manager_object import CardContractManager
from selenium.webdriver.support.ui import Select
import time
class CardContractExpired:
    def __init__(self):
        print()


    @staticmethod
    def card_contract_expired(driver):
        cardContractExpired = CardContractManager(driver)

        # 进入左侧菜单：“购买”
        cardContractExpired.go_purhase_obj().click()
        time.sleep(2)

        # 切换至储值卡合同管理
        cardContractExpired.card_contarct_manager_obj().click()
        time.sleep(2)

        # 下拉框选择门店
        Select(cardContractExpired.select_store_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 搜索按钮
        cardContractExpired.search_obj().click()
        time.sleep(2)

        # 选择要修改的储值卡合同
        cardContractExpired.select_contract_obj().click()
        time.sleep(2)

        # 鼠标移至“更多”
        cardContractExpired.more_menu_obj()
        time.sleep(2)

        # 选择修改合同的有效期
        cardContractExpired.edit_validity_period_obj().click()
        time.sleep(2)

        # 输入合同的开始时间
        cardContractExpired.time_from_obj().send_keys("2018-09-01")
        time.sleep(2)

        # 输入合同的结束时间
        cardContractExpired.time_to_obj().send_keys("2018-09-05")
        time.sleep(2)

        # 输入备注
        cardContractExpired.note_obj().send_keys("自动化修改合同的有效期")

        # 确认
        cardContractExpired.confirm_button_obj().click()

        # 弹框确认
        cardContractExpired.bullet_box_confirm().click()













