from selenium import webdriverw
driver = webdriver.chrome()
driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.find_element_by_name("q").send_keys("javatpoint")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
print("sample testcases successfully completed")
