'''
coding=utf-8
User:Tina
Data:2018-07-20
添加场地
'''
from pageObject.site_info_object import SitePage
import time


class AddSite:

    def __init__(self):
        print("Add Store...")

    @staticmethod
    def add_site(driver):
        addsite = SitePage(driver)

        # 设置按钮
        addsite.setting_obj().click()
        time.sleep(2)

        # 切换至门店信息table
        addsite.store_obj().click()
        time.sleep(2)

        # 选择门店
        addsite.store_select_data_obj().click()
        time.sleep(2)

        # 查看
        addsite.detail_button_obj().click()
        time.sleep(2)

        # 添加场地
        addsite.site_add_obj().click()
        time.sleep(2)

        # 添加场地名称
        addsite.site_name_obj().send_keys("场地1")

        # 可容纳人数
        addsite.people_number_obj().send_keys("50")

        # 保存
        addsite.site_save_button_obj().click()

