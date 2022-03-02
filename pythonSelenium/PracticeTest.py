import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browserName = "Chrome"
driver = ""
str_cur_workingdir = os.getcwd()
str_driver_executable_path = str_cur_workingdir+"\\browserdrivers"
print(str_driver_executable_path)

if browserName.upper() == "CHROME":
    from selenium.webdriver.chrome.service import Service
    s = Service(str_driver_executable_path+"\\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    # opt.add_argument("--headless")  # To launch the browser in headless mode
    opt.add_argument('--disable-infobars')
    opt.add_argument('--no-sandbox')
    # opt.add_argument('start-maximized') # To start the browser in maximize window
    opt.add_argument('--disable-extensions')
    opt.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=s, options=opt)

elif browserName.upper() == "FIREFOX":
    from selenium.webdriver.firefox.service import Service
    s = Service(str_driver_executable_path + "\\geckodriver.exe")
    driver = webdriver.Firefox(service=s)
elif browserName.upper() == "EDGE":
    from selenium.webdriver.edge.service import Service
    s = Service(str_driver_executable_path + "\\msedgedriver.exe")
    driver = webdriver.Edge(service=s)
else:
    print("Invalid Browser")

driver.implicitly_wait(60)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Bure Ramana")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("bure.ramanamurthy@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Welcome")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()

dropdown_gender = driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1")
elm_dropDown_gender = Select(dropdown_gender)
elm_dropDown_gender.select_by_index(1)
time.sleep(4)
elm_dropDown_gender.select_by_visible_text("Male")
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
elm_success_message = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']")
str_message = elm_success_message.text
print("Message : "+str_message)
assert "success" in str_message
print("Test Passed")
