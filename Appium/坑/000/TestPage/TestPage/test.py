
import os
import time
from appium import webdriver


img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
time =time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_save_path = img_folder + time + '.png'
driver.get_screenshot_as_file(screen_save_path)

