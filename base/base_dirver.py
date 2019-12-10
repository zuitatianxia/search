import os, sys
sys.path.append(os.getcwd())
from appium import webdriver
def init_driver():
     #server 启动参数
     from appium.webdriver.common.touch_action import TouchAction
     desired_caps = {}
     # 设备信息
     desired_caps['platformName'] = 'Android'
     desired_caps['platformVersion'] = '5.1'
     desired_caps['deviceName'] = '192.168.56.101:5555'
     # app信息
     desired_caps['appPackage'] = 'com.android.settings'
     desired_caps['appActivity'] = '.Settings'
     desired_caps['unicodeKeyboard'] = True
     desired_caps['resetKeyboard'] = True
     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
     return driver