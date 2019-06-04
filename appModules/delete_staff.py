'''
coding=utf-8
User:Tina
data:2018-11-30
删除员工
'''

from pageObject.staff_list_object import StaffList
class DeleteStaff:
    def __init__(self):
        print("删除会籍销售以及教练")

    @staticmethod
    def delete_staff(driver,nickname):
        deletestaff = StaffList(driver)

        # 左侧菜单栏：“员工”
        deletestaff.go_staff_page_obj().click()

        # 选择删除的数据
        deletestaff.data_selected_obj(nickname).click()

        # 点击删除按钮
        deletestaff.delete_button_obj().click()

        # 浏览器的确认弹框
        deletestaff.confirm_obj()

        # 删除成功提示
        deletestaff.delete_success_obj().click()





