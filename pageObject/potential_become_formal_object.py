'''
coding=utf-8
User:Tina
Data:2018-08-28
潜在客户变成正式会员页面元素封装
'''

from util.object_map import *


class PotentitalBecomeFormal:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    #左侧菜单栏：客户
    def go_customer_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[3]/a/i')
        return element

    #进入正式会员列表
    def go_member_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="会员管理"]')
        return element

    # 选择潜在客户
    def potentital_customer_select_obj(self):
        element = getElement(self.driver,'xpath','//table[@class="table-1"]//tr[1]//td[1]')
        return element

    # 点击入会
    def admission_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="入会"]')
        return element

    # 性别
    def sex_select_obj(self):
        element = getElement(self.driver,'id','sex_1')
        return element

    # 选择开卡门店
    def store_select_obj(self):
        element = getElement(self.driver,'name','shop_id')
        return element

    # 选择销售人员——定位下拉框
    def sales_select_obj(self):
        element = getElement(self.driver,'name','staff_id')
        return element

    # 定位下拉框中的文本框
    def sales_input_obj(self):
        element = getElement(self.driver,'xpath','//input[@class="select2-search__field"]')
        return element

    # 选择卡种名称
    def card_select_obj(self):
        element = getElement(self.driver,'name','product_id')
        return element

    # 生成合同编号
    def bianhao_add_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="renew lay-small contract_set lay-wrap"]//input[@name="sn"]')
        return element

    # 下一步
    def next_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="row-in"]//button[@class="btn-small next"]')
        return element

    # 保存
    def save_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="row-in"]//button[@class="btn-small save"]')
        return element

    # 取消收取押金
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[@class="lay-btn-cancel"]')
        return element


