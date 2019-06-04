'''
coding=utf-8
User:Tina
Data:2018-08-28
潜在客户详情页面元素封装
'''

from util.object_map import *


class PotentitalCustomer:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    #左侧菜单栏：客户
    def go_customer_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[3]/a/i')
        return element

    # 添加潜在客户
    def potentital_customer_add_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="tab_icon hastips"]//a[@class="icon_club new"]')
        return element

    # 姓名
    def nickname_input_obj(self):
        element = getElement(self.driver,'name','nickname')
        return element

    # 性别
    def sex_select_obj(self):
        element = getElement(self.driver,'id','sex_1')
        return element

    # 手机
    def mobile_input_obj(self):
        element = getElement(self.driver,'name','mobile')
        return element

    # 选择会籍销售
    def sales_id_select_obj(self):
        element = getElement(self.driver,'name','sales_id')
        return element

    # # 会籍销售下拉框
    # def sales_idSelectObj(self):
    #     element = getElement(self.driver,'xpath','//span[@class="select2-selection__arrow"]')
    #     return element
    #
    # # 会籍销售下拉框中输入框
    # def sales_inputValueObj(self):
    #     element = getElement(self.driver,'xpath','//input[@class="select2-search__field"]')
    #     return element

    # 渠道属性
    def channel_property_select_obj(self):
        element = getElement(self.driver,'name','channel_property')
        return element

    # 获取渠道
    def source_channel_select_obj(self):
        element = getElement(self.driver,'name','source_channel')
        return element

    # 保存
    def save_button_odj(self):
        element = getElement(self.driver,'xpath','//button[text()="保存"]')
        return element

    # 确认
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element




