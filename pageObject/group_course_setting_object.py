'''
coding=utf-8
Tina 2018-08-20
团课课程设置的页面封装
'''
from util.object_map import *
from util.opeartion_json import OperetionJson

class GroupCourseSetting:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.opera_json = OperetionJson()

    # 添加团课
    # 进入左侧菜单栏——课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[4]/a/i')
        return element

    # 进入团课课程设置的table
    def go_group_course_setting_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="团课课程设置"]')
        return element

    # 团课课程设置页面的添加
    def add_group_course_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer add"]')
        return element

    # 团课课程添加页面的新增团课名字
    def add_course_name_obj(self):
        element = getElement(self.driver,'name','name')
        return element

    # 团课课程添加页面的新增团课时间
    def add_course_time_obj(self):
        element = getElement(self.driver,'name','course_minutes')
        return element

    # 团课课程添加页面的新增团课支持的门店
    def add_course_store_obj(self):
        element = getElement(self.driver, 'xpath', '//label[contains(text(),"懒猫馆——测试数据不能删除")]')
        return element

    # 团课课程添加页面的新增团课教练
    def add_course_coach_obj(self):
        element = getElement(self.driver, 'xpath', '//label[contains(text(),"懒猫管的团课及私教教练不允许删除")]')
        return element

    # 团课预约另付费：是
    def pay_setting_obj(self):
        element = getElement(self.driver,'id','fee_type_1')
        return element


    # 付费团课储值卡扣费设置
    # 团课储值卡付费设置(付费按钮)
    def pay_card_setting_obj(self,course_name):
        element = getElement(self.driver,'xpath','//td[text()="{}"]/following-sibling::td[4]/i[3]'.format(course_name))
        return element

    # 团课付费选择储值卡
    def select_card_obj(self):
        element = getElement(self.driver,'xpath','//td[text()="储值卡不要删除数据"]/preceding-sibling::td[1]//input')
        return element

    # 团课付费输入设置的金额
    def money_setting_obj(self):
        element = getElement(self.driver,'xpath','//td[text()="储值卡不要删除数据"]/following-sibling::td[1]//input')
        return element

    # 付费设置页面的确定按钮
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//button[@class="btn-medium save"]')
        return element

    # 确认
    def add_confirm_obj(self):
        element = getElement(self.driver, 'xpath', '//a[text()="确定"]')
        return element

    # 再次确认
    def queding_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="lay-btn-confirm"]')
        return element

    # 管理员代预约付费的团课
    def select_group_course_obj(self):
        course_text =self.opera_json.get_data("test02_add_pay_group_course")
        print(course_text)
        element = getElement(self.driver,'xpath','')


    # 删除团课课表
    def delete_course_obj(self,course_name):
        element= getElement(self.driver,'xpath','//td[contains(text(),"{}")]/../td[5]/i[4]'.format(course_name))
        return element

    # 删除的确认按钮
    def confirm_delete_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element

    # 删除成功提示：确定
    def cancel_success_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element