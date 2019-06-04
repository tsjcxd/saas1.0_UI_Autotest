'''
coding=utf-8
Tina 2018-11-30
储值卡列表
'''

from util.object_map import *
class StoreCardList:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        print("封装页面：会籍卡设置")

    # 左侧菜单：购买
    def go_purchase_menu_obj(self):
        element = getElement(self.driver, 'xpath', '//*[@id="mCSB_1_container"]/li[5]/a/i')
        return element

    # 储值卡设置
    def go_store_card_setting_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="储值卡设置"]')
        return element

# 选择需要被编辑的卡的数据
    def data_selected_obj(self,cardname):
        element = getElement(self.driver,'xpath','//table[@class="table-1 edit-mode"]//td[text()="{}"]'.format(cardname))
        return element

    # 点击禁售
    def banned_sale_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="禁售"]')
        return element

    # 是否确定禁止售卖：确定
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element

    # 删除成功，弹框确认
    def delete_success_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element