
'''
coding=utf-8
Tina 2018-09-03
编辑私教合同的有效期
'''

from pageObject.private_contract_manager_object import PrivateContractManager
from selenium.webdriver.support.ui import Select
import time


class PrivateContractExpired:
    def __init__(self):
        print()

    def private_contract_expired(driver):
        privateContractExpired = PrivateContractManager(driver)
        driver.implicitly_wait(30)

        # 进入左侧菜单：“购买”
        privateContractExpired.go_purchase_menu_obj().click()

        # 切换至私教合同管理
        privateContractExpired.go_private_contract_manager().click()

        # 下拉框选择门店
        Select(privateContractExpired.select_store_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 搜索按钮
        privateContractExpired.search_obj().click()
        time.sleep(3)

        # 选择要修改的私教合同
        privateContractExpired.select_contract_obj().click()

        # 鼠标移至“更多”
        privateContractExpired.more_menu_obj()
        time.sleep(2)

        # 选择修改合同的有效期
        privateContractExpired.edit_validity_period_obj().click()

        # 输入合同的开始时间
        privateContractExpired.time_from_obj().send_keys("2018-09-01")
        time.sleep(2)

        # 输入合同的结束时间
        privateContractExpired.time_to_obj().send_keys("2018-09-05")
        time.sleep(2)

        # 输入备注
        privateContractExpired.note_obj().send_keys("自动化修改合同的有效期")

        # 确认
        privateContractExpired.confirm_button_obj().click()

        # 弹框确认
        privateContractExpired.bullet_box_confirm().click()
