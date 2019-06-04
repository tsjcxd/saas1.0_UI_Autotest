'''
coding=utf-8
Tina 2018-07-20
添加员工（教练）
'''


from pageObject.coach_staff_info_object import CoachInfo
import random

class AddCoach:

    def __init__(self):
        print("add staff")

    @staticmethod
    def add_coach(driver,name):
        addcoach =CoachInfo(driver)
        driver.implicitly_wait(30)

        # 左侧菜单：员工
        addcoach.go_staff_page_obj().click()
        # time.sleep(2)

        # 添加员工按钮
        addcoach.membership_sales_add_obj().click()
        # time.sleep(2)

        # 工号
        addcoach.employee_id_input_obj().send_keys(random.randint(1000000,1999999))

        # 昵称
        addcoach.nickname_input_obj().send_keys(name)

        # 登录账号
        addcoach.loginname_input_obj().send_keys(str(random.choice(["Tsj","Auto"]))+str(random.randint(10000000000,19999999999)))

        # 密码
        addcoach.password_input_obj().send_keys("123456")

        # 真实姓名
        addcoach.realname_input_obj().send_keys("教练自动化测试")

        # 性别选择
        addcoach.sex_select_obj().click()
        # time.sleep(2)

        # 门店选择
        addcoach.shop_select_obj().click()
        # time.sleep(2)

        # 手机号码
        addcoach.mobile_input_obj().send_keys(str(random.randint(10000000000,19999999999)))

        # 角色选择
        addcoach.role_select_coach1_obj().click()
        # time.sleep(2)
        addcoach.role_select_coach2_obj().click()
        # time.sleep(2)

        # 保存
        addcoach.save_button_obj().click()

        # 确认
        addcoach.confirm_button_obj().click()

        # time.sleep(3)


