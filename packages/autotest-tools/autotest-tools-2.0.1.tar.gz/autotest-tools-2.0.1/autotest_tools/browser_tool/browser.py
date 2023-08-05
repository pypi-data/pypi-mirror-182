from selenium import webdriver

from autotest_tools.log_tool.logtest import LogTest

TAG = "BrowserCommon"


class BrowserCommon(object):

    @staticmethod
    def init_browser(browser_name):
        """
        获取浏览器驱动
        :param browser_name: 浏览器类型
        :return: 浏览器驱动
        """
        LogTest.debug(TAG, "Init browser: browser_name is {}".format(browser_name))
        options = webdriver.ChromeOptions()
        options.add_argument("ignore-certificate-errors")
        if browser_name not in webdriver.__all__ or "Chrome" == browser_name:
            browser = webdriver.Chrome(options=options)
        else:
            browser = getattr(webdriver, browser_name)()
        return browser
