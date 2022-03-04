import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browserName = "Chrome"
str_URL = "https://the-internet.herokuapp.com/"
driver = ""
str_cur_workingdir = os.getcwd()
str_driver_executable_path = str_cur_workingdir + "\\browserdrivers"

if browserName.upper() == "CHROME":
    from selenium.webdriver.chrome.service import Service

    s = Service(str_driver_executable_path + "\\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    # opt.add_argument("--headless")  # To launch the browser in headless mode
    opt.add_argument('--disable-infobars')
    opt.add_argument('--no-sandbox')
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

print(browserName + " browser started successfully!!!")
# driver.implicitly_wait(60)  # Global and waits for 60 seconds for object if it is not shown.
driver.get(str_URL)
driver.maximize_window()
wait = WebDriverWait(driver, 60)

elm_multiple_windows = driver.find_element(By.XPATH,"//a[text()='Multiple Windows']")
elm_multiple_windows.click()

elm_click_here_link = driver.find_element(By.XPATH,"//a[text()='Click Here']")
elm_click_here_link.click()

handles = driver.window_handles
parent_window_handle = handles[0]
child_window_handle = handles[1]

driver.switch_to(child_window_handle)

elm_heading = driver.find_element(By.XPATH,"//h3")
print(elm_heading.text)

