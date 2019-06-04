'''
coding=utf-8
User:Tina
Data:2018-08-23
会员：“测试数据不要删除(18321829313)”购买储值卡：“储值卡不要删除数据”页面元素封装
'''

from util.object_map import *


class PurchaseStoredCard:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    #左侧菜单栏：客户
    def go_customer_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[3]/a/i')
        return element

    # 切换至会员列表
    def go_customer_manager_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="会员管理"]')
        return element

    # 定位顶部搜索会员的输入框
    def search_bar_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="top_search"]')
        return element

    # 筛选会员：“测试数据不要删除(18321829313)”
    def search_customer_obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content"]//li[text()="测试数据不要删除(18321829313)"]')
        return element

    # 选中会员：“测试数据不要删除(18321829313)”
    def selected_customer_obj(self):
        element = getElement(self.driver,'xpath','//input[@value="15799323"]')
        return element

    # 买储值卡
    def purchase_card_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="买储值卡"]')
        return element

    # 选择开卡门店
    def store_obj(self):
        element = getElement(self.driver,'name','shop_id')
        return element

    # 选择销售人员
    def sales_obj(self):
        element = getElement(self.driver,'name','staff_id')
        return element

    # 选择卡种名称
    def card_obj(self):
        element = getElement(self.driver,'name','product_id')
        return element

    # 合同编号
    def bianhao_obj(self):
        element = getElement(self.driver,'name','sn')
        return element

    # 下一步
    def next_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="下一步"]')
        return element

    # 确认支付
    def save_button_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="确认支付"]')
        # element = getElement(self.driver,'xpath','//*[@id="lay-body-1"]/div[3]/div[1]/div[2]/div/div[22]/button')
        return element

    # 确定
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element
