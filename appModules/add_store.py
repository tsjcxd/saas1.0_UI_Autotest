'''
coding=utf-8
User:Tina
Data:2018-07-20
添加门店
'''
from pageObject.shop_info_object import SettingPage
from selenium.webdriver.support.ui import Select
import time


class AddStore:

    def __init__(self):
        print("Add Store...")

    @staticmethod
    def add_store(driver,storename,storephone,selectvalue1,selectvalue2,selectvalue3,storedetailadress):
        addstore = SettingPage(driver)

        # 设置按钮
        addstore.setting_obj().click()
        time.sleep(2)

        # 切换至门店信息table
        addstore.store_obj().click()
        time.sleep(2)

        # 添加门店按钮
        addstore.store_add_obj().click()
        time.sleep(2)

        # 添加门店名字
        addstore.store_add_name_obj().send_keys(storename)

        # 电话号码
        addstore.store_add_phone_obj().send_keys(storephone)

        # 选择省
        Select(addstore.store_add_province_id_obj()).select_by_value(selectvalue1)

        # 选择市
        Select(addstore.store_add_city_id_obj()).select_by_value(selectvalue2)

        # 选择区
        Select(addstore.store_add_district_id_obj()).select_by_value(selectvalue3)

        # 填写详细的地址
        addstore.store_add_detail_address_obj().send_keys(storedetailadress)

        # 保存
        addstore.store_save_button_obj().click()

        # 确认
        addstore.store_add_success_obj().click()
        time.sleep(3)

