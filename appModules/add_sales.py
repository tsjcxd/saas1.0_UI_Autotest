'''
coding=utf-8
Tina 2018-07-20
添加员工（会籍销售）
'''


from pageObject.sales_staff_Info_object import SalesInfo
import time
import random
class AddSales:

    def __init__(self):
        print("add staff")

    @staticmethod
    def add_salse(driver,name):
        addsales =SalesInfo(driver)

        # 左侧菜单：员工
        addsales.go_staff_page_obj().click()
        time.sleep(2)

        # 添加员工按钮
        addsales.membership_sales_add_Obj().click()
        time.sleep(2)

        # 工号
        addsales.employee_id_input_obj().send_keys(random.randint(1000000,1999999))

        # 昵称
        addsales.nickname_input_obj().send_keys(name)

        # 登录账号
        addsales.loginname_input_obj().send_keys(str(random.choice(["Tsj","Auto"]))+str(random.randint(10000000000,19999999999)))

        # 密码
        addsales.password_input_obj().send_keys("123456")

        # 真实姓名
        addsales.realname_input_obj().send_keys("会籍销售自动化测试")

        # 性别选择
        addsales.sex_select_obj().click()
        time.sleep(2)

        # 门店选择
        addsales.shop_select_obj().click()
        time.sleep(2)

        # 手机号码
        addsales.mobile_input_obj().send_keys(str(random.randint(10000000000,19999999999)))

        # 角色选择
        addsales.role_select_sales_obj().click()
        time.sleep(3)

        # 保存
        addsales.save_button_obj().click()
        time.sleep(2)

        # 确认
        addsales.confirm_button_obj().click()

        time.sleep(5)


