
import os
import time
from urllib import request
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
driver = None

@pytest.fixture(scope="class")
def setup1(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name=='chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name=='firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name=='IE':
        driver=webdriver.Ie(IEDriverManager().install())
    elif browser_name=='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
    #     # web_driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    request.cls.driver = driver
    yield
    driver.close()
    driver=None

# # confest.Theme function defined py
# def _fail_picture():
#     fail_picture()
# def fail_picture(self):
#         f = self.get_screenshot_as_file()
#         allure.attach.file(f, 'Failed with Example screenshot: {filename}'.format(filename=f), 	allure.attachment_type.PNG)
# def get_screenshot_as_file(self):
#         '''Function on the local theme'''
#         try:
#             pic_pth = self.conf.pic_path
#             filename = pic_pth + str(time.time()).split('.')[0] + '.png'
#             filename = filename.replace('\\', '/')
#             self.webdriver.get_screenshot_as_file(filename)
#             self.log.debug('get_screenshot_as_file {filename}'.format(filename=filename))
#             return filename
#         except Exception as e:
#             self.log.error(e)
#             return None
#
#
#  # Write the hook function
#  # Failure use of an automatic function screenshot
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#          hook pytest failure
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         _fail_picture()
#
#
#


def driver_init_1(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # web_driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
    # web_driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub',desired_capabilities={
    #         "browserName": "firefox",
    #         "platformName": "linux",
    #     })
    # web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
    web_driver=webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
@pytest.fixture(scope="class")
def driver_init_2(request):
    # firefox_options=webdriver.FirefoxOptions()
    # firefox_options.set_headless()
    # web_driver = webdriver.Firefox(firefox_options=firefox_options,executable_path="geckodriver.exe")
    # web_driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4444/wd/hub')
    web_driver = webdriver.Firefox(executable_path="geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()
=======
import os
import time
from urllib import request
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
driver = None

@pytest.fixture(scope="class")
def setup1(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name=='chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name=='firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name=='IE':
        driver=webdriver.Ie(IEDriverManager().install())
    elif browser_name=='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
    #     # web_driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    request.cls.driver = driver
    yield
    driver.close()
    driver=None

# # confest.Theme function defined py
# def _fail_picture():
#     fail_picture()
# def fail_picture(self):
#         f = self.get_screenshot_as_file()
#         allure.attach.file(f, 'Failed with Example screenshot: {filename}'.format(filename=f), 	allure.attachment_type.PNG)
# def get_screenshot_as_file(self):
#         '''Function on the local theme'''
#         try:
#             pic_pth = self.conf.pic_path
#             filename = pic_pth + str(time.time()).split('.')[0] + '.png'
#             filename = filename.replace('\\', '/')
#             self.webdriver.get_screenshot_as_file(filename)
#             self.log.debug('get_screenshot_as_file {filename}'.format(filename=filename))
#             return filename
#         except Exception as e:
#             self.log.error(e)
#             return None
#
#
#  # Write the hook function
#  # Failure use of an automatic function screenshot
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#          hook pytest failure
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         _fail_picture()
#
#
#


def driver_init_1(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # web_driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
    # web_driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub',desired_capabilities={
    #         "browserName": "firefox",
    #         "platformName": "linux",
    #     })
    # web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
    web_driver=webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
@pytest.fixture(scope="class")
def driver_init_2(request):
    # firefox_options=webdriver.FirefoxOptions()
    # firefox_options.set_headless()
    # web_driver = webdriver.Firefox(firefox_options=firefox_options,executable_path="geckodriver.exe")
    # web_driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4444/wd/hub')
    web_driver = webdriver.Firefox(executable_path="geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()

