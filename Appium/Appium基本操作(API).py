https://www.cnblogs.com/forcepush/p/6721828.html
python -m pydoc -p 4895

Appium定位顺序
1、ID
2、class
3、uiautomator
4、xpath
5、accessibility_id(即content-desc)





//另外，原生和H5混合页面，XPath比较好用：
driver.findElementByXPath("//android.widget.TextView[contains(@text,'账户')]").click();

driver.findElementByXPath("//android.view.View[contains(@resource-id,'switchAccount')]").click();

driver.findElementByXPath("//android.view.View[contains(@content-desc,'绑定')]").click();

'''
获取当前页面所有可点击的按钮？？
Listelements = driver.find_element_by_xpath("//*")
print (Listelements)
'''


//切换框架
driver.switch_to.active_element
driver.switch_to.alert
driver.switch_to.default_content
driver.switch_to.frame
driver.switch_to.window
driver.switch_to.window('main')

driver.switch_to.default_content()
driver.switch_to.frame('frame_name')
driver.switch_to.frame(1)
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
切回父框架：driver.switch_to.parent_frame()


定位
orientation = driver.orientation

driver.name


search_button = driver.find_element_by_id("su")  # 百度搜索按钮
# 现在我们获取百度一下的值
value = search_button.get_attribute("value")  # 获取input标签的value，也就是百度一下那4个字
print(value)   # 打印  百度一下


'''
Appium在webdriver基础上增加
find_element_by_accessibility_id()
find_elements_by_accessibility_id()
find_element_by_android_uiautomator()
find_element_by_android_uiautomator()
'''
API
'''
find_element_by_accessibility_id     ###就是content-description属性
find_element_by_android_uiautomator    ###可定位任何元素
find_element_by_class_name
find_element_by_css_selector
find_element_by_id
find_element_by_link_text
find_element_by_name
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_xpath
'''



'''元素定位'''
通过name 定位  name 就是text
driver.find_element_by_name("1").click()

'''id 定位  resource-id'''
driver.find_element_by_id("com.android.calculator2:id/digit1").click()

driver.find_element_by_id('com.lizi.app:id/setting_imageView').click() 

'''class name 定位'''
使用 ClassName 一般获得的 view 都不止一个，所以应该需要遍历一遍得到的 views，然后缩写搜索
条件来获得目标控件。示例中因为只有一个 textview 控件在窗口上面，所以不需要遍历。
driver.find_element_by_class_name("android.widget.RelativeLayout")

或者
buttons = driver.find_elements_by_class_name("android.widget.Button")
#第一个元素
buttons.pop(0).click()
#第二个元素
buttons.pop(1).click()
#最后个元素
buttons.pop().click()


'''以accessibility_id进行定位，对Android而言，就是content-description属性
鉴于这是一个隐藏属性，而 Android 上用于查找控件的各种属性可能有所缺失或者有重复（比如 id
重复，比如一个 list 下面的所有项可能都是叫做“id/text1”），所以最佳的办法就是跟开发团队沟通好每个
view 都赋予一个唯一的 contentDescription。
所以，为了便于自动化测试的开展，需要和开发同学沟通好，为每一个控件添加 contentDescription 属
性。
'''
driver.find_element_by_accessibility_id('push_button').click() 
driver.find_element_by_accessibility_id("天猫超市").click()


'''android uiautomator 定位
一个元素的任意属性都可以通过 android uiautomator 方法来进行定位，但要保证这种定位方
式的唯一性。'''
driver.find_element_by_android_uiautomator('new UiSelector().text("Custom View")').click()         #text
driver.find_element_by_android_uiautomator('new UiSelector().textContains("View")').click()        #textContains
driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("Custom")').click()    #textStartsWith
driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^Custom.*")').click()    #textMatches
#className
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Custom View")').click()     
#classNameMatches
driver.find_element_by_android_uiautomator('new UiSelector().classNameMatches(".*TextView$").text("Custom View")').click()  

#resourceId
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/text1")')    
#resourceIdMatches
driver.find_element_by_android_uiautomator('new UiSelector().resourceIdMatches(".*id/text1$")')

driver.find_element_by_android_uiautomator('new UiSelector().clickable(true).text("Custom View")').click() 

'''xpath 定位
Appium对于xpath定位执行效率是比较低的，也就是说遇到xpath的定位代码的时候，执行比较慢。迫不得已的情况下尽量不用这个定位方式。
'''

my_home = driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()  


'''
当前我的索引是4，底部一共有5个按钮，说明索引是从0开始算。本篇我们要学习xpath定位，
但是xpath索引是从1开始计算的。利用xpath定位的思路是：先根据class定位到五个元素，
然后根据索引5来精确定位到“我的”模块。
'''
# 点击“我的”  
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='4']").click()  
time.sleep(2)  
# 点击“我的关注“  
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='3']").click()  
time.sleep(2)  
# 点击“麦克风“  
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='2']").click()  
time.sleep(2)  
# 点击““视频  
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='1']").click()  
time.sleep(2)  
# 点击“默认主页“  
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='0']").click()  


'''driver.find_element_by_ios_uiautomation()'''



截图代码
img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\Screenshots\\'
#####F:\githubup\Appium\Hachi\src\screenshots\
timestamp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
#####显示时间格式为201712240326
screen_save_path = img_folder + timestamp + '.png'
driver.get_screenshot_as_file(screen_save_path)

================================================================================================================================
获取手机name    连接手机   
CMD  →   adb devices

================================================================================================================================

1、安装应用
driver.install_app()
driver.install_app('path/to/my.apk')
driver.install_app("D:\\android\\apk\\ContactManager.apk")

2、卸载应用
driver.remove_app()
driver.remove_app('com.example.android.apis')

3、关闭应用
driver.close_app()
关闭打开的应用，默认关闭当前打开的应用，所以不需要入参。

4、检查应用是否安装
driver.is_app_installed()
检查应用是否已经安装。需要传参应用包的名字。返回结果为 Ture 或 False。
例：
driver.is_app_installed('com.example.android.apis')

5、启动应用  6、关闭应用
关闭应用。这个方法与 quit()有所不同，quit()是在结果测试时执行的，这个方法并非真正的关闭应用，
相当于按 home 键将应用置于后台，可以通过 launch_app()再次启动。

driver.launch_app()
driver.close_app()


配合driver.close_app() 使用的
