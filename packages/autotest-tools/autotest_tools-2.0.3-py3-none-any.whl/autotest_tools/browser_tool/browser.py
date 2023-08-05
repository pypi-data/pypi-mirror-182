import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from autotest_tools.config_tool.conf_common import ConfCommon
from autotest_tools.log_tool.logtest import LogTest

TAG = "BrowserCommon"
option = ConfCommon("options.ini").get_section_dict("browser options")


class BrowserCommon(object):

    @staticmethod
    def init_browser(model=None, grid=None):
        """
        获取浏览器驱动
        :param model: 浏览器模式
        :param grid: grid地址
        :return: 浏览器驱动
        """
        LogTest.debug(TAG, "Init browser: model is {}".format(model))
        is_headless = True if platform.system() == 'Linux' else False
        if model == "debug" or is_headless:
            options = webdriver.ChromeOptions()
            options.add_argument(option["headless"])
            options.add_argument(option["disable-gpu"])
            options.add_argument(option["user-agent"])
            options.add_argument(option["window-size"])
            options.add_argument(option["disable-infobars"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            browser = webdriver.Remote(command_executor=grid, options=options)
            browser.implicitly_wait(10.0)
        else:
            service = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=service)
            browser.maximize_window()
            browser.implicitly_wait(10.0)
        return browser
