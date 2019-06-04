'''
coding=utf-8
Tina 2018-08-23
正式会员购买储值卡
'''

from pageObject.purchase_stored_card_object import PurchaseStoredCard
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.keys import Keys
import time



class PurchaseCard:
    def __init__(self):
        print(" Customer Purchase Store Card")

    #正式会员购买会籍卡
    @staticmethod
    def purchase_card(driver):
        purchaseCard =PurchaseStoredCard(driver)

        # 左侧菜单栏"客户"
        purchaseCard.go_customer_obj().click()
        time.sleep(2)

        # 搜索会员“测试数据不要删除(18321829313)”
        purchaseCard.search_bar_obj().click()
        purchaseCard.search_bar_obj().send_keys("18321829313")
        purchaseCard.search_customer_obj().click()
        time.sleep(2)

        # 选择搜索结果：“测试数据不要删除(18321829313)”
        purchaseCard.selected_customer_obj().click()

        # 点击购买储值卡
        purchaseCard.purchase_card_obj().click()
        time.sleep(2)

        # 选择门店
        Select(purchaseCard.store_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 选择销售人员
        Select(purchaseCard.sales_obj()).select_by_visible_text("测试会籍销售不要删除")

        # 选择卡名称
        Select(purchaseCard.card_obj()).select_by_visible_text("储值卡不要删除数据")

        # 填写合同编号
        purchaseCard.bianhao_obj().send_keys(str(random.randint(100000,199999)))
        time.sleep(3)

        # 下一步
        purchaseCard.next_obj().click()
        time.sleep(3)

        # 保存
        purchaseCard.save_button_obj().click()
        time.sleep(3)

        # 确认
        purchaseCard.confirm_button_obj().click()
        time.sleep(2)
