__author__ = 'TANUKI'
#python3.5+selenium打开chrome浏览器，去掉ignore-certificate-errors提示

class OpenChrome(unittest.TestCase):

    def setUp(self):
           #打开chrome浏览器，路径中双斜杠
            self.chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = self.chromedriver
           #去掉提示
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            self.driver= webdriver.Chrome(self.chromedriver,chrome_options=options)
           #最大化
            self.driver.maximize_window()

            # 隐性等待
            self.driver.implicitly_wait(30)
            self.base_url = "http://www.baidu.com"
            self.verificationErrors = []
            self.accept_next_alert = True

     def test_open_chrome(self):
            driver = self.driver
            driver.get(self.base_url)
            try: self.assertEqual("百度一下，你就知道", driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))