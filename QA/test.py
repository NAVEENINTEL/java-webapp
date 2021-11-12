

import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

print("sample test case started")
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
# navigate to the url
driver.get("http://localhost:8080/")
# identify the Google search text box and enter the value
driver.find_element_by_name("username").send_keys("javatpoint")
driver.find_element_by_name("password").send_keys("javatpoint")
time.sleep(3)
# close the browser
driver.close()
print("sample test case successfully completed")
