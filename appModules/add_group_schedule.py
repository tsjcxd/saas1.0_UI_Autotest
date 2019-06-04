'''
coding=utf-8
Tina 2018-07-20
添加团课排期
'''

from selenium.webdriver.support.ui import Select
from pageObject.group_schedule_object import GroupSchedule
from datetime import datetime
import time


class AddGroupSchedule:

    def __init__(self):
        print("add GroupSchedule")

    @staticmethod
    def add_group_schedule(driver,course_time,course_name):
        addgroupschedule = GroupSchedule(driver)
        driver.implicitly_wait(30)

        # 进入左侧菜单“课程”
        addgroupschedule.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至团课课表table
        addgroupschedule.go_group_schedule_obj().click()
        time.sleep(3)

        # 新增
        addgroupschedule.add_group_schedule_obj().click()

        # 添加团课的详情页--选择门店
        Select(addgroupschedule.add_course_store_obj()).select_by_visible_text("懒猫馆——测试数据不能删除")

        # 添加团课的详情页--选择场地
        Select(addgroupschedule.add_course_site_obj()).select_by_visible_text("场地1")

        # 添加团课的详情页--选择时间
        addgroupschedule.add_course_time_obj().send_keys(course_time)

        current = datetime.now().weekday()
        coach = "coach_id_" + str(current)

        # 添加团课的详情页--选择当天的免费课程
        Select(addgroupschedule.select_course_store_obj(current)).select_by_visible_text(course_name)
        # 添加团课的详情页--选择当天的课程的教练
        Select(addgroupschedule.select_course_coach_obj(coach)).select_by_visible_text("懒猫管的团课及私教教练不允许删除")

        # 确认，新增成功
        addgroupschedule.add_confirm_obj().click()
        time.sleep(2)

        # 新增成功后，点击确认按钮
        addgroupschedule.course_schedule_confirm_obj().click()
        time.sleep(3)

