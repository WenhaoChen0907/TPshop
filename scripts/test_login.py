import os,sys

sys.path.append(os.getcwd())
import allure


import pytest

from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("login_data", key)



class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    """
    @pytest.mark.parametrize(("username","pwd","toast"), data_with_key("test_login"))
    def test_login(self, username, pwd, toast):
        # 1.点击我的
        # 2.点击登录/注册,前两步写在page的init中，因为1不属于登录页面2每次都需要这两步
        # 3.输入用户名
        self.login_page.input_username(username)
        # 4.输入密码
        self.login_page.input_password(pwd)
        # 5.点击登录
        self.login_page.click_login()
        # 6.判断是否登录成功
        assert self.login_page.is_toast_exist(toast)
    """

    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        # 1.点击我的
        # 2.点击登录/注册,前两步写在page的init中，因为1不属于登录页面2每次都需要这两步
        # 3.输入用户名
        allure.attach('输入用户名', args["username"])
        self.login_page.input_username(args["username"])
        # 4.输入密码
        allure.attach('输入密码', args["password"])
        self.login_page.input_password(args["password"])
        # 5.点击登录
        allure.attach('点击登录', '')
        self.login_page.click_login()



        # 6.判断是否登录成功
        allure.attach('判断提示的信息是否存在', args["toast"])
        res = self.login_page.is_toast_exist(args["toast"], True, args["screen"])
        # allure上传图片
        allure.attach("图片", open('./screen/'+ args["screen"] +'.png', 'rb').read(), allure.attach_type.PNG)
        assert res




