'''
coding=utf-8
User:Tina
Date:2018-08-22
教练（团课/私教）详情页面的封装
'''
from util.object_map import *

class CoachInfo:
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(30)

    # 左侧菜单栏：员工
    def go_staff_page_obj(self):
        element = getElement(self.driver,'xpath','/html/body/div[1]/div[1]/div[1]/ul/div[1]/div/li[6]/a/i')
        return element

    # 添加
    def membership_sales_add_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer new"]')
        return element

    # 工号
    def employee_id_input_obj(self):
        element = getElement(self.driver,'name','employee_id')
        return element

    # 昵称
    def nickname_input_obj(self):
        element = getElement(self.driver,'name','nickname')
        return element

    # 登录账号
    def loginname_input_obj(self):
        element = getElement(self.driver,'name','login_name')
        return element

    # 密码
    def password_input_obj(self):
        element = getElement(self.driver,'name','login_pwd')
        return element

    # 真实姓名
    def realname_input_obj(self):
        element = getElement(self.driver,'name','realname')
        return element

    # 性别
    def sex_select_obj(self):
        element = getElement(self.driver,'xpath','//input[@id="sex_1"]')
        return element

    # 门店
    def shop_select_obj(self):
        element =getElement(self.driver,'xpath','//label[contains(text(),"懒猫馆——测试数据不能删除")]')
        return element

    # 手机号码
    def mobile_input_obj(self):
        element = getElement(self.driver,'name','mobile')
        return element

    # 角色——团课教练
    def role_select_coach1_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="row"][9]//label[text()="团课教练"]')
        return element

    # 角色——私教教练
    def role_select_coach2_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="row"][9]//label[text()="私教教练"]')
        return element

    # 保存
    def save_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@id="staff_set"]//input[@class="btn-small save"]')
        return element

    # 确认
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element