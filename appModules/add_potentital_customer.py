'''
coding=utf-8
Tina 2018-07-20
添加潜在客户
'''

from pageObject.potentital_customer_object import PotentitalCustomer
from selenium.webdriver.support.ui import Select
import random




class AddPotentitalCustomer:
    def __init__(self):
        print("add Potentital Customer ")

    #添加一个潜在的客户
    @staticmethod
    def add_potentital_customer(driver,nickname):
        addcustomer = PotentitalCustomer(driver)
        driver.implicitly_wait(30)

        # 左侧菜单栏"客户"
        addcustomer.go_customer_obj().click()
        # time.sleep(2)

        # 潜在客户添加按钮
        addcustomer.potentital_customer_add_obj().click()
        # time.sleep(2)

        # 添加姓名
        addcustomer.nickname_input_obj().send_keys(nickname)

        # 选择性别
        addcustomer.sex_select_obj().click()
        # time.sleep(2)

        # 添加手机
        addcustomer.mobile_input_obj().send_keys(str(random.randint(10000000000,19999999999)))

        # 添加会籍销售
        Select(addcustomer.sales_id_select_obj()).select_by_visible_text("测试会籍销售不要删除")
        # addcustomer.sales_idSelectObj().click()
        # addcustomer.sales_inputValueObj().send_keys(selectvalue1,Keys.ENTER)
        # time.sleep(2)

        # 添加渠道属性
        Select(addcustomer.channel_property_select_obj()).select_by_visible_text("人力推广")

        # 获取渠道
        Select(addcustomer.source_channel_select_obj()).select_by_visible_text("外出获取")

        # 保存
        addcustomer.save_button_odj().click()
        # time.sleep(2)


        # 确认
        addcustomer.confirm_button_obj().click()
        # time.sleep(5)















