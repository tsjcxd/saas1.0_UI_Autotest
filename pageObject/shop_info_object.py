'''
coding=utf-8
User:Tina
Data:2018-08-28
门店信息页面元素封装
'''

from util.object_map import *


class SettingPage:

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    #设置
    def setting_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="icon_club setting"]')
        return element

    # 切换至门店
    def store_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="门店信息"]')
        return element

    # 添加按钮
    def store_add_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer new"]')
        return element

    # 门店名字
    def store_add_name_obj(self):
        element = getElement(self.driver,'name','shop_name')
        return element

    # 电话号码
    def store_add_phone_obj(self):
        element = getElement(self.driver,'name','phone')
        return element

    # 省
    def store_add_province_id_obj(self):
        element = getElement(self.driver,'name','province_id')
        return element

    # 市
    def store_add_city_id_obj(self):
        element = getElement(self.driver,'name','city_id')
        return element

    # 区
    def store_add_district_id_obj(self):
        element = getElement(self.driver,'name','district_id')
        return element

    # 详细地址
    def store_add_detail_address_obj(self):
        element = getElement(self.driver,'name','address')
        return element

    # 保存
    def store_save_button_obj(self):
        element = getElement(self.driver,'xpath','//input[@class="btn-small save"]')
        return element

    # 确认
    def store_add_success_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="lay-btn-confirm"]')
        return element

    # 选中被删除的测试数据
    def store_delete_data_obj(self):
        element = getElement(self.driver,'xpath','//table[@class="table-1 edit-mode"]//td[contains(text(),"自动化")]')
        return element

    # 删除按钮
    def store_delete_button_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer del"]')
        return element

    # 确认删除
    def delele_cofirm_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[@class="lay-btn-confirm"]')
        return element

    # 删除成功提示
    def delete_success_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element


