'''
coding=utf-8
User:Tina
Data:2018-08-27
正式会员:“测试数据不要删除(18321829313)”购买私教：“私教课程测试不要删除”
'''

from pageObject.purchase_private_course_object import PurchasePrivateCourse
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.keys import Keys
import time
from util.opeartion_json import OperetionJson



class PurchasePrivateContract:
    def __init__(self):
        print(" Purchase Private Contract")


    #正式会员购买私教合同
    @staticmethod
    def purchase_private_course(driver):
        purchaseprivatecourse =PurchasePrivateCourse(driver)
        opera_json = OperetionJson()


        # 左侧菜单栏"客户"
        purchaseprivatecourse.go_customer_obj().click()
        time.sleep(2)

        # 搜索会员“测试数据不要删除(18321829313)”
        purchaseprivatecourse.search_bar_obj().click()
        purchaseprivatecourse.search_bar_obj().send_keys("18321829313")
        purchaseprivatecourse.search_customer_obj().click()
        time.sleep(2)

        # 选择搜索结果：“测试数据不要删除(18321829313)”
        purchaseprivatecourse.selected_customer_obj().click()

        # 点击购买私教
        purchaseprivatecourse.purchase_private_course_obj().click()
        time.sleep(2)

        # 选择门店
        Select(purchaseprivatecourse.store_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 选择销售人员
        Select(purchaseprivatecourse.sales_obj()).select_by_visible_text("测试教练不要删除")

        # 选择上课教练
        Select(purchaseprivatecourse.coach_obj()).select_by_visible_text("测试教练不要删除")

        # 选择课程
        Select(purchaseprivatecourse.course_obj()).select_by_visible_text(opera_json.get_data("test01_add_private_course"))

        # 选择价格级别
        Select(purchaseprivatecourse.price_level_obj()).select_by_visible_text("1级(1~10节)")

        # 填写购买数量
        purchaseprivatecourse.count_obj().send_keys(10)

        # 填写合同编号
        purchaseprivatecourse.bianhao_obj().send_keys(str(random.randint(100000,199999)))

        # 下一步
        purchaseprivatecourse.next_obj().click()
        time.sleep(2)

        # 保存
        purchaseprivatecourse.confirm_obj().click()
        time.sleep(2)

        # 确认
        purchaseprivatecourse.queding_obj().click()
        time.sleep(2)
