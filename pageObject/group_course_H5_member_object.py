'''
coding=utf-8
Tina 2018-08-30
会员端预约团课页面的封装
'''
from util.object_map import *
from util.opeartion_json import OperetionJson
class GroupCourse_H5Member:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.opera_json = OperetionJson()

    # 切换至底部的课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//li[@class="course"]//span[text()="课程"]')
        return element

    # 定位周二
    def weekdays_tues_obj(self):
        element = getElement(self.driver,'xpath','//li[@name="seven_days_select"]//p[@class="weekday" and text()="二"]')
        return element

    # 定位周四
    def weekdays_thur_obj(self):
        element = getElement(self.driver,'xpath','//li[@name="seven_days_select"]//p[@class="weekday" and text()="四"]')
        return element

    # 定位场馆
    def store_select_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="shop_show"]')
        return element

    def store_select1_obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="shop_content"]//li[@data="369627602"]')
        return element

    # 团课列表预约
    def appoint_obj(self):
        element = getElement(self.driver, 'xpath','//ul[@class="list-2"]/li/descendant::span[contains(text(),"{}")]/ancestor::a'.format(self.opera_json.get_data("test01_add_free_group_course")))
        return element

    # 团课详情页面预约
    def appoint_detail_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="btn-large order"][text()="预约"]')
        return element

    # 弹框确认
    def confirm_obj(self):
        self.driver.switch_to_alert().accept()

