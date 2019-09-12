from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.9.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    # 解决不能输入中文的问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # toast
    desired_caps['automationName'] = 'Uiautomator2'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver