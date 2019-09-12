from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    mine_button = By.XPATH, "text,我的"
    login_signup_button = By.XPATH, "text,登录/注册"

    username_text_button = By.XPATH, "text,请输入手机号码"
    password_text_button = By.ID, "com.tpshop.malls:id/pwd_et"
    login_button = By.ID, "com.tpshop.malls:id/login_tv"

    def __init__(self, driver):
        super().__init__(driver)
        # 1.点击我的
        # 2.点击登录/注册
        self.jump_2_login_page()

    def jump_2_login_page(self):
        self.click(self.mine_button)
        self.click(self.login_signup_button)

    def input_username(self, text):
        self.send_keys(self.username_text_button, text)

    def input_password(self, text):
        self.send_keys(self.password_text_button, text)

    def click_login(self):
        self.click(self.login_button)






