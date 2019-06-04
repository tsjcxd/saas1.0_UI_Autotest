'''
coding=utf-8
Tina 2018-08-22
添加会籍卡
'''

from util.object_map import *
class AddMembershipCard:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        print("封装页面：会籍卡设置")

    # 左侧菜单：购买
    def go_purchase_menu_obj(self):
        element = getElement(self.driver, 'xpath', '//*[@id="mCSB_1_container"]/li[5]/a/i')
        return element

    # 会籍卡设置
    def go_card_setting_obj(self):
        element = getElement(self.driver, 'xpath', '//a[text()="会籍卡设置"]')
        return element

    # 添卡
    def add_card_obj(self):
        element = getElement(self.driver, 'xpath', '//a[text()="添卡"]')
        return element

    # 添加卡的名称
    def name_obj(self):
        element = getElement(self.driver, 'xpath', '//div[@class="box-2"]//input[@name="title"]')
        return element

    #卡类型
    def card_type_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="box-2"]//select[@name="card_type"]')
        return element

    #有效天数
    def unit_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="box-2"]//input[@name="unit"]')
        return element

    # 售卖基础价格
    def price_obj(self):
        element = getElement(self.driver, 'name', 'price')
        return element

    # 转让手续费
    def fee_obj(self):
        element = getElement(self.driver, 'name', 'fee')
        return element

    # 可售卖门店
    def shop_select_obj(self):
        element = getElement(self.driver, 'xpath', '//div[@class="box-a1 max-height-4a overflow-scroll"]//label[text()="懒猫馆——测试数据不能删除"]')
        return element

    # 售卖时间
    def saletime_from_obj(self):
        element = getElement(self.driver, 'xpath', '//div[@class="columns-7"]//input[@name="valid_from"]')
        return element

    # 售卖时间
    def saletime_to_obj(self):
        element = getElement(self.driver, 'xpath', '//div[@class="columns-7"]//input[@name="valid_to"]')
        return element

    # 可在线购买
    def purchase_obj(self):
        element = getElement(self.driver, 'id', 'online_1')
        return element

    # 排序权重
    def weights_obj(self):
        element = getElement(self.driver, 'name', 'weight')
        return element

    # 确定
    def confirm_obj(self):
        element = getElement(self.driver, 'xpath', '//a[text()="确定"]')
        return element

    # 确认
    def confirm_button_obj(self):
        element = getElement(self.driver, 'xpath', '//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element


