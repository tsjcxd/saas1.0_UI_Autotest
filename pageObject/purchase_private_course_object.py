'''
coding=utf-8
User:Tina
Data:2018-08-27
会员：“测试数据不要删除(18321829313)”购买私教合同：“私教课程测试不要删除”的页面的封装
'''

from util.object_map import *


class PurchasePrivateCourse:
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

    # 点击买私教
    def purchase_private_course_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="买私教"]')
        return element

    # 选择开卡门店
    def store_obj(self):
        element = getElement(self.driver,'name','shop_id')
        return element

    # 选择销售人员
    def sales_obj(self):
        element = getElement(self.driver,'name','staff_id')
        return element

    # 选择上课教练
    def coach_obj(self):
        element = getElement(self.driver,'name','coach_id')
        return element

    # 选择课程名称
    def course_obj(self):
        element = getElement(self.driver,'name','course_cat_id')
        return element

    # 选择价格级别
    def price_level_obj(self):
        element = getElement(self.driver,'name','price_level')
        return element

    # 填写购买数量
    def count_obj(self):
        element = getElement(self.driver,'xpath','//*[@name="count"]')
        return element

    # 输入合同编号
    def bianhao_obj(self):
        element = getElement(self.driver,'name','sn')
        return element

    # 下一步
    def next_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="renew lay-small contract_set lay-wrap"]//button[text()="下一步"]')
        return element

    # 确认
    def confirm_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="renew lay-small contract_set lay-wrap"]//button[text()="确认支付"]')
        return element

    # 弹框确定
    def queding_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element