'''
coding=utf-8
Tina 2018-08-23
潜在客户变成正式会员
'''

from pageObject.potential_become_formal_object import PotentitalBecomeFormal
from selenium.webdriver.support.ui import Select
import random
import time



class FormalCustomer:
    def __init__(self):
        print("Potentital Customer Change to Formal Customer ")

    #潜在客户变成正式会员
    @staticmethod
    def formalCustomer(driver):
        addformalCustomer = PotentitalBecomeFormal(driver)

        # 左侧菜单栏"客户"
        addformalCustomer.go_customer_obj().click()
        time.sleep(2)

        # 选择潜在客户“潜客——自动化测试勿删除”
        addformalCustomer.potentital_customer_select_obj().click()
        time.sleep(2)

        # 点击入会
        addformalCustomer.admission_obj().click()
        time.sleep(2)

        # 选择开卡门店
        Select(addformalCustomer.store_select_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 选择销售人员
        Select(addformalCustomer.sales_select_obj()).select_by_visible_text("测试会籍销售不要删除")

        # addformalCustomer.salesSelectObj().click()
        # time.sleep(2)
        # addformalCustomer.salesInputObj().send_keys(sales,Keys.ENTER)
        # time.sleep(2)


        # 选择卡种名称
        Select(addformalCustomer.card_select_obj()).select_by_visible_text("测试会籍卡不要删除")

        # 填写合同编号
        addformalCustomer.bianhao_add_obj().send_keys(str(random.randint(1000000,1999999)))

        # 下一步
        addformalCustomer.next_button_obj().click()
        time.sleep(2)

        # 保存
        addformalCustomer.save_button_obj().click()
        time.sleep(2)

        # 确认
        addformalCustomer.confirm_button_obj().click()
        time.sleep(2)

        # 左侧菜单栏"客户"
        addformalCustomer.go_customer_obj().click()
        time.sleep(2)

        # 切换table至“正式会员”
        addformalCustomer.go_member_obj().click()












