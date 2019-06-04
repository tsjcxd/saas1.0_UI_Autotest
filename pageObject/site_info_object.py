'''
coding=utf-8
User:Tina
Data:2018-08-28
场地信息页面元素封装
'''
from util.object_map import *


class SitePage:

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    # 进入设置页面
    def setting_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="icon_club setting"]')
        return element

    # 切换至门店table
    def store_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="门店信息"]')
        return element

    # 选中门店
    def store_select_data_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="content_wrap"]//table[@class="table-1 edit-mode"]//td[contains(text(),"自动化")]')
        return element

    # 查看按钮
    def detail_button_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer info"]')
        return element

    # 添加场地
    def site_add_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="添加场地"]')
        return element

    # 场地名称
    def site_name_obj(self):
        element = getElement(self.driver,'name','space_name')
        return element

    # 容纳人数
    def people_number_obj(self):
        element = getElement(self.driver,'name','apply_limit')
        return element

    # 保存
    def site_save_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="columns-4 save_button"]/input[2]')
        return element

