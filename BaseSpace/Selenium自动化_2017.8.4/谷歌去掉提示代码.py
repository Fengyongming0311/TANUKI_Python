__author__ = 'TANUKI'
#python3.5+selenium��chrome�������ȥ��ignore-certificate-errors��ʾ

class OpenChrome(unittest.TestCase):

    def setUp(self):
           #��chrome�������·����˫б��
            self.chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = self.chromedriver
           #ȥ����ʾ
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            self.driver= webdriver.Chrome(self.chromedriver,chrome_options=options)
           #���
            self.driver.maximize_window()

            # ���Եȴ�
            self.driver.implicitly_wait(30)
            self.base_url = "http://www.baidu.com"
            self.verificationErrors = []
            self.accept_next_alert = True

     def test_open_chrome(self):
            driver = self.driver
            driver.get(self.base_url)
            try: self.assertEqual("�ٶ�һ�£����֪��", driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))