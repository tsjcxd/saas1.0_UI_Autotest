'''
coding=utf-8
Tina 2018-08-20
删除门店
'''
from pageObject.shop_info_object import SettingPage
from selenium.webdriver.support.ui import Select
import time

class DeleteStore:

    def __init__(self):
        print("Delete Store...")

    @staticmethod
    def deletestore(driver):
        deletestore = SettingPage(driver)

        # 设置
        deletestore.setting_obj().click()
        time.sleep(2)

        # 切换至门店信息的table
        deletestore.store_obj().click()
        time.sleep(2)

        # 选择删除的门店的数据
        deletestore.store_delete_data_obj().click()
        time.sleep(2)

        # 点击删除按钮
        deletestore.store_delete_button_obj().click()
        time.sleep(2)

        # 确认删除
        deletestore.delele_cofirm_obj().click()

        # 删除成功的弹框提示
        deletestore.delete_success_obj().click()





