from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver


    def click(self, loc):
        self.find_element(loc).click()

    def send_keys(self, loc, text):
        self.find_element(loc).send_keys(text)


    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./screen/" + file_name + ".png")

    # 自定义函数，调用系统函数，只是重名而已
    def find_element(self, loc, timeout=10.0, poll=2.0):
        # return self.driver.find_element(loc[0], loc[1])
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath_with_feature(loc_value)

        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(loc_by, loc_value))

    def find_elements(self, loc, timeout=10.0, poll=2.0):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath_with_feature(loc_value)

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(loc_by, loc_value))


    def find_toast(self, message, is_screenshot=False, screen_name=None, timeout=3, poll=0.1):
        loc = By.XPATH, "//*[contains(@text, '" + message + "')]"
        ele = self.find_element(loc, timeout, poll)

        if is_screenshot:
            self.screenshot(screen_name)

        return ele.text


    def is_toast_exist(self,  message, is_screenshot=False, screen_name=None, timeout=3, poll=0.1):
        try:
            self.find_toast(message, is_screenshot, screen_name, timeout, poll)
            return True
        except Exception:
            return False


    # xpath工具类
    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature


    # xpath工具类
    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc


