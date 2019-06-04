'''
参数化
'''
import datetime
class parameterize:
    def get_params(self,name):
        data_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        parameterize = "{}{}".format(name,data_now)
        return parameterize






# if __name__ == "__main__":
#     Para = parameterize()
#     Grop_name = Para.get_params("团课")
#     print(Grop_name)


# class Parameters:
#
#     def get_params(self,name):
#         data_now = datetime.datetime.now().date()
#         params = "自动化{}{}".format(name,data_now)
#         return params
#
#
# if __name__ == "__main__":
#     para = Parameters()
#     params = para.get_params("团课测试")
#     print(params)