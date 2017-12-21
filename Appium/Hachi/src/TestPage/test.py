public class dealWebView {
    private AndroidDriver<?> driver;
    private boolean isInstall = false;
    private String userName="youremail";
    private String password="yourpassword";
    /**
     * @author Young
     * @throws IOException
     */
    public void startRecord() throws IOException {
        Runtime rt = Runtime.getRuntime();
        // this code for record the screen of your device
        rt.exec("cmd.exe /C adb shell screenrecord /sdcard/runCase.mp4");

    }

    @BeforeClass(alwaysRun = true)
    public void setUp() throws Exception {
        // set up appium

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability(CapabilityType.BROWSER_NAME, "");
        capabilities.setCapability("platformName", "Android");
        capabilities.setCapability("deviceName", "Android Emulator");
        capabilities.setCapability("platformVersion", "5.1");
        // if no need install don't add this
        if (isInstall) {
            File classpathRoot = new File(System.getProperty("user.dir"));
            File appDir = new File(classpathRoot, "apps");
            File app = new File(appDir, "zhihu.apk");
            capabilities.setCapability("app", app.getAbsolutePath());
        }
        capabilities.setCapability("appPackage", "com.zhihu.android");
        // support Chinese
        capabilities.setCapability("unicodeKeyboard", "True");
        capabilities.setCapability("resetKeyboard", "True");
        // no need sign
        capabilities.setCapability("noSign", "True");
        //capabilities.setCapability("autoWebview", "True");
        capabilities.setCapability("appActivity", ".ui.activity.GuideActivity");
        driver = new AndroidDriver<WebElement>(new URL(
                "http://127.0.0.1:4723/wd/hub"), capabilities);
        startRecord();
    }

    @Test
    public void loginWithMicroBlog() throws InterruptedException {

        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        // swipe to right
        driver.findElementById("com.zhihu.android:id/login_and_register")
                .click();
        driver.findElementById("com.zhihu.android:id/btn_social").click();
        driver.findElementById("com.zhihu.android:id/login_weibo").click();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        Thread.sleep(15000);
        Set<String> context = driver.getContextHandles();
        for (String contextName : context) {
            System.out.println(contextName);

        }
//        driver.context("WEBVIEW");
        System.out.println(driver.getPageSource());
        driver.findElementsByClassName("android.widget.EditText").get(0).sendKeys(
                userName);
        driver.findElementsByClassName("android.widget.EditText").get(1).sendKeys(
                password);
        driver.findElementByXPath("//android.view.View[contains(@content-desc,'登录')]").click();

    }

    @AfterClass(alwaysRun = true)
    public void tearDown() throws Exception {
        driver.quit();
    }
}