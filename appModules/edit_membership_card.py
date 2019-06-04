'''
coding=utf-8
User:Tina
data:2018-11-30
会籍卡禁售
'''

from pageObject.membership_card_list_object import MembershipCardList
class EditMembershipCard:
    def __init__(self):
        print("删除会籍销售以及教练")

    @staticmethod
    def edit_membership_card(driver,cardname):
        edit_membership_card = MembershipCardList(driver)

        # 左侧菜单栏：“售卖”
        edit_membership_card.go_purchase_menu_obj().click()

        # 会籍卡设置
        edit_membership_card.go_card_setting_obj().click()

        # 选择要禁售的会籍卡的名字
        edit_membership_card.data_selected_obj(cardname).click()

        # 点击禁售
        edit_membership_card.banned_sale_obj().click()

        # 确认
        edit_membership_card.confirm_button_obj().click()

        # 删除成功之后确认提示
        edit_membership_card.delete_success_obj().click()
