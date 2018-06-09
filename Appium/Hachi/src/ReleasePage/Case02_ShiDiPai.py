__author__ = 'TANUKI'
#coding:utf-8
#from appium import webdriver
import time

###
import sys
sys.path.append("..")
from FilePublic_Page import Public_Page
import huadong
############################################
"""
        生产环境流程：
        点击7个推荐模块      RecommendApp
        点击图片实地派会员（专享权益）
        点击尊享服务中的
        1.智能家居
        2.社区公告
        3.专项活动
        下滑
        页面
        点击图片广告广州常春藤楼盘
        点击推荐楼盘
        无锡玫瑰庄园
        惠州常春藤
        广州蔷薇国际
        点击更多楼盘
        点击进入
        广州常春藤
        无锡玫瑰庄园
        惠州常春藤
        广州蔷薇国际
        武汉君兰汀岸
        天津海棠雅著
        :return: None
        """
############################################
class ShiDiPai:
    def IntoShiDiPai(driver):
        #先点击实地派按钮进入首页页面
        Public_Page.Switch_Navigation(driver, tab = "实地派")

    def RecommendApp(driver):
        """
        7个推荐应用和更多
        """
        try:
            #测试全部应用(7个+更多)
            time.sleep(5)
            item = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_app_name")
            for dondake in item:
                case = dondake.text
                ShiDiPai.Hachilist_app(driver, case)
        except Exception as e:
            print (e)
            pass

    def Brand_Image(driver):
        """
        点击商标图片——实地派会员专享权益
        :return: None
        """
        time.sleep(2)
        case = "实地派会员专享权益"
        try:
            driver.find_element_by_id('com.pujitech.pujiejia:id/iv_brand_image').click()
            time.sleep(5)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print("测试点击%s用例Passed............成功" % case)
        except:
            print("测试点击%s用例失败............Failed" % case)
            time.sleep(2)
            pass

    def ZunXiangFuWu(driver):
        # (1)测试尊享服务中智能家居是否可以进入
        time.sleep(2)
        case = "智能家居"
        try:
            dower = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_modules_name")
            for target in dower:
                if target.text == case:
                    target.click()
                    break
                # 点完了就跳出循环，否则会再次找寻case内容导致报错
            time.sleep(6)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_base_title")
            if checkpoint.text == case or checkpoint.text == '我的网关':
                driver.back()
                print("测试点击%s用例Passed............成功" % case)
            else:
                print("标题为%s...不在应用列表中，请重新确认标题名称。" % checkpoint.text)
                driver.back()
                print("测试点击%s用例失败............Failed" % case)

        except:
            print("测试点击%s用例失败............Failed" % case)
            time.sleep(2)
            pass

        # (2)测试尊享服务中社区公告是否可以进入
        time.sleep(3)
        case = "社区公告"
        try:
            gonggao = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_modules_name")
            for target in gonggao:
                if target.text == case:
                    target.click()
                    break
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_announcement_name").click()
                # 点击一条公告查看公告内容
                time.sleep(2)
                driver.wait_activity(".modules.usercenter.community.views.activities.AnnouncementDetailActivity", 30)
                tv_title = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
                if tv_title.text == '公告详情':
                    driver.back()
                else:
                    print("查看社区公告详情失败......显示标题为%s" % tv_title.text)
                    driver.back()
                driver.back()
                # 这个退出社区公告页面回到首页
                print("测试点击%s用例Passed............成功" % case)
            else:
                driver.back()
                print("测试点击%s用例失败............Failed" % case)
        except:
            print("测试点击%s用例失败............Failed" % case)
            time.sleep(2)
            pass

        # (3)测试专享活动是否可以进入
        time.sleep(5)
        case = "专享活动"
        try:
            # 进入专享活动
            zhuanxiang = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_modules_name")
            for target in zhuanxiang:
                if target.text == case:
                    target.click()
                    break
            time.sleep(3)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

            print("测试点击%s用例Passed............成功" % case)
        except:
            print("测试点击%s用例失败............Failed" % case)
            time.sleep(2)
            pass

    def XiaLaPage(driver):
        """
        下滑页面以显示推荐楼盘
        :return: None
        """
        time.sleep(2)
        huadong.shanghua(driver, 300)

    def Community_Image(driver):
        """
        点击主要推荐的大图片楼盘iv_community_image
        :return: None
        """
        time.sleep(2)
        case = "图片广告广州常春藤楼盘"
        try:
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_community_image").click()
            # 滑动查看常春藤
            time.sleep(2)
            huadong.shanghua(driver, 300)

            time.sleep(2)
            huadong.shanghua(driver, 300)

            driver.back()
            print("测试点击%s用例Passed............成功" % case)
        except:
            print("测试点击%s用例失败............Failed" % case)
            time.sleep(2)

    def Recommend_Community_Title(driver):
        """
        实地派页面中的文字推荐楼盘，目前有无锡玫瑰庄园、惠州常春藤、广州蔷薇国际
        :return: None
        """
        tuijianbuild = ["无锡玫瑰庄园", "惠州常春藤", "广州蔷薇国际"]
        # print ("点击进入各个推荐楼盘点击进入各个推荐楼盘")
        try:
            for case in tuijianbuild:
                lpan = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_community_name")
                for target in lpan:
                    if target.text == case:
                        target.click()
                        ShiDiPai.tuijianloupan(driver, case)
                        break
                        # 点完了就跳出循环，否则会再次找寻case内容导致报错
        except Exception as e:
            print ("点击文字推荐楼盘报错信息为:",e)
            pass

    def More_Building(driver):
        """
        点击更多楼盘，进入精品楼盘页面查看

        原来是原生的精品楼盘页面变为H5...无法进行定位
        :return: None
        """
        time.sleep(3)
        huadong.shanghua(driver, 800)
        lpmoredict = {"广州常春藤": "广州常春藤 23000元/m² 广东广州黄埔区禾丰路与永和大道交汇处 智慧社区 优质学府 全能配套 百万大城",
                      "无锡玫瑰庄园": "无锡玫瑰庄园 8000元/m² 江苏无锡惠山区中惠大道与曙光南路交汇处 地铁口 价格洼地 高铁旁",
                      "惠州常春藤": "惠州常春藤 价格待定 广东惠州惠阳区惠南大道旁 轻轨学府",
                      "广州蔷薇国际": "广州蔷薇国际 20000元/m² 广东广州增城区荔城街实地蔷薇国际 智能社区 叠水园林 品质大盘 地铁沿线",
                      "武汉君兰汀岸": "武汉君兰汀岸 17000元/m² 湖北武汉汉阳区经济技术开发区小军山大道19号",
                      "天津海棠雅著": "天津海棠雅著 9300元/m² 天津天津宝坻区津蓟高速温泉城出口西侧500米 品质大盘 全龄配套 智能大盘 低密度"}
        try:
            # driver.find_elements_by_id("com.pujitech.pujiejia:id/ll_more_community").click()
            driver.find_element_by_android_uiautomator('new UiSelector().text("更多楼盘")').click()

            driver.wait_activity(".modules.h5.views.activitys.CommonH5Activity", 30)
            time.sleep(3)
            '''
            for (name, element) in lpmoredict.items():
                try:
                    driver.find_element_by_accessibility_id("%s" % element).click()
                    ShiDiPai.tuijianloupan(driver, name)

                except Exception as e:
                    print("精品楼盘点击楼盘详情报错:", e)
                    print("测试进入%s楼盘用例失败............Failed" % name)
            time.sleep(3)
            '''
            title = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if title.text == "精品楼盘":
                driver.back()
            else:
                print("检测到该页面标题与测试点不符......请查看当前为%s的测试点标题......" % title.text)
                driver.back()
            print("首页测试结束...")

        except Exception as e:
            print("进入精品楼盘报错为：", e)
            pass

    def Hachilist_app(driver, case):
        """
        全部应用（如果有改动改这里）
        还有更多的话也可以作为普通页面点击
        ["餐饮美食", "社区商城", "服务预定", "课程培训",
        "限时促销", "精品团购",
        "社区公告", "房屋报修", "物业缴费", "投诉建议",
        "精品楼盘", "专享活动", "投资理财", u"智能手环", u"手机开门", u"消费分期", u"智能家居", u"哈奇贝壳",
        "更多"]

        其中["投诉建议", "房屋报修"] 点击后判断是否为业主
        哈奇贝壳怎么是空白页
        """
        application = ["餐饮美食", "社区商城", "服务预定", "课程培训","限时促销", "精品团购",
                  "社区公告", "物业缴费","精品楼盘", "专享活动", "投资理财","更多", u"消费分期"]
        time.sleep(3)
        if case in application:
            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
                time.sleep(4)

                checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
                if checkpoint.text == case or checkpoint.text == "握手分期"\
                    or checkpoint.text == "握手金融":
                    driver.back()
                else:
                    print ("标题为%s...不在应用列表中，请重新确认标题名称。"%checkpoint.text)
                    driver.back()
                print("测试点击%s用例Passed............成功"%case)
            except:
                print("测试点击%s用例失败............Failed"%case)
                time.sleep(2)
                pass
        elif case == "投诉建议" or case == "房屋报修" or case == u"手机开门":
            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
                time.sleep(8)

                checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_content")
                if checkpoint.text == "您没有在该小区认证房间":
                    print("点击%s后提示："%case, checkpoint.text)
                    driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
                    print("测试点击%s用例Passed............成功" % case)
                else:
                    Public_Page.ExitBack(driver)
                    print("测试点击%s用例Passed............成功" % case)


            except:
                print("测试点击%s用例失败............Failed"%case)
                time.sleep(2)
                pass
        elif case == u"智能家居":
            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
                time.sleep(6)

                checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_base_title")
                if checkpoint.text == "我的网关":
                    driver.back()
                else:
                    print("标题为%s...不在应用列表中，请重新确认标题名称。"%checkpoint.text)
                    driver.back()
                print("测试点击%s用例Passed............成功"%case)
            except:
                print("测试点击%s用例失败............Failed"%case)
                time.sleep(2)
                pass
        elif case == u"智能手环":
            try:
                driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%case).click()
                time.sleep(8)
                #点击手环进入我家页面，暂时判断页面是否有全部应用元素
                ##################以后优化，每隔1秒执行一次循环，然后直到找到元素，退出整体循环
                checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/all_application_tv")
                if checkpoint.text == "全部应用":
                    retap = "实地派"
                    try:
                        driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
                        time.sleep(2)
                        allbutn = driver.find_elements_by_id("com.pujitech.pujiejia:id/fixed_bottom_navigation_title")
                        for target in allbutn:
                            if target.text == retap:
                                target.click()
                                break
                            # 点完了就跳出循环，否则会再次找寻case内容导致报错
                        print("测试点击%s用例Passed............成功" % case)
                        time.sleep(3)
                        #为了下一次循环等待3s
                    except:
                        print("未切换到首页页面，程序退出....")
                        print("测试点击%s用例失败............Failed" % case)
                        pass


                else:
                    print ("没有找到%s,在当前页面,请重新检查测试脚本..."%checkpoint.text)
                    print("测试点击%s用例失败............Failed" % case)
                    time.sleep(2)

            except:
                pass
        else:
            pass

    def tuijianloupan(driver, case):
        # 点击每个推荐楼盘
        time.sleep(3)
        try:
            # 向上滑动查看页面
            driver.wait_activity(".modules.h5.views.activitys.CommonH5Activity", 30)
            time.sleep(2)
            huadong.shanghua(driver, 500)
            time.sleep(2)
            huadong.shanghua(driver, 500)
            time.sleep(2)
            huadong.xiahua(driver, 500)
            time.sleep(2)
            huadong.xiahua(driver, 500)

            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            print ("测试进入%s楼盘用例Passed............成功"%case)
        except Exception as e:
            print ("测试进入%s楼盘用例失败............Failed"%case)
            print ("报错信息为:",e)
            time.sleep(2)
            pass

    def Building_Name_Container(driver):
        """
        选择标题进入切换楼盘页面
        :return: None
        """
        driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/rl_building_name_container").click()






