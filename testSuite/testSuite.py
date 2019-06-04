'''
coding=utf-8
User:Tina
data:2018-08-29
用例集
'''

import HTMLTestRunner
import unittest
import os
import datetime


from testScripts.test_setting import Setting
from testScripts.test_card_setting import TestCard
from testScripts.test_add_staff import TestAddStaff
from testScripts.test_add_potentital_customer import TestCustomer
from testScripts.test_add_group_course import TestGroupCourse
from testScripts.test_add_private_course import TestPrivateCourse
from testScripts.test_purchase_contract import TestPurchaseContract
from testScripts.test_member_appoint_H5 import TestMemberAppoint_H5
from testScripts.test_admin_appoint_PC import TestAdminAppointCourse_PC
from testScripts.test_edit_contract_time import TestEditCardContract
from testScripts.test_delete_course import TestDeleteCourse

# 按照不同的模块运行

# 运行：添加门店及场地
testSettingStore = unittest.TestLoader().loadTestsFromTestCase(Setting)
#
# 运行：添加卡设置(会籍卡和储值卡)
testCard = unittest.TestLoader().loadTestsFromTestCase(TestCard)

# 运行：添加员工（会籍销售和教练）
testAddStaff = unittest.TestLoader().loadTestsFromTestCase(TestAddStaff)

# 运行：添加潜在客户（潜在客户入会）
testAddCustomer = unittest.TestLoader().loadTestsFromTestCase(TestCustomer)



# 运行：添加团课以及团课设置
testGroupCourse = unittest.TestLoader().loadTestsFromTestCase(TestGroupCourse)

# 运行：添加私教课程以及私教课程设置
testPrivateCourse = unittest.TestLoader().loadTestsFromTestCase(TestPrivateCourse)


# 运行:购买私教课程和储值卡
testPurchasecontract = unittest.TestLoader().loadTestsFromTestCase(TestPurchaseContract)


# 运行：会员端预约团课以及私教课程
testMemberAppoint_H5 = unittest.TestLoader().loadTestsFromTestCase(TestMemberAppoint_H5)


# 运行：PC端预约团课以及私教课程
testAdminAppoint_PC = unittest.TestLoader().loadTestsFromTestCase(TestAdminAppointCourse_PC)



# 运行：编辑会员的私教合同以及储值卡合同
testEditCardContract = unittest.TestLoader().loadTestsFromTestCase(TestEditCardContract)


# 运行：删除全部课程
testDeleteCourse = unittest.TestLoader().loadTestsFromTestCase(TestDeleteCourse)

# 全部流程
# suite = unittest.TestSuite([testSettingStore,testCard,testAddStaff,testAddCustomer])

# 主流程
suite = unittest.TestSuite([testGroupCourse,testPrivateCourse,testPurchasecontract,testMemberAppoint_H5,testAdminAppoint_PC,testEditCardContract,testDeleteCourse])

# 生成HTML的报告
curPath = os.path.dirname(os.path.dirname(__file__))
time = datetime.datetime.now().date()
filepath = r"{}\testReport\myreport{}.html".format(curPath,time)
fp = open(filepath,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="SaaS Club Online Regression Testing")
runner.run(suite)
fp.close()











