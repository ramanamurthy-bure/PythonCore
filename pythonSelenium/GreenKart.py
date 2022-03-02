import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browserName = "Chrome"
str_URL = "https://rahulshettyacademy.com/seleniumPractise"
driver = ""
str_cur_workingdir = os.getcwd()
str_driver_executable_path = str_cur_workingdir + "\\browserdrivers"

if browserName.upper() == "CHROME":
    from selenium.webdriver.chrome.service import Service

    s = Service(str_driver_executable_path + "\\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")  # To launch the browser in headless mode
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

str_title = driver.title
print("URL '" + str_URL + "' launched successfully and \nnavigated to the page titled : '" + str_title + "'")

elm_veg_search_textbox = driver.find_element(By.XPATH, "//input[@type='search']")
elm_veg_search_textbox.click()
time.sleep(1)
elm_veg_search_textbox.send_keys("ber")
time.sleep(3)
print("Entered 'ber' in the search text box")

elm_veg_search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
elm_veg_search_button.click()
print("Clicked on 'search' veg icon")

elm_veg_search_results = driver.find_elements(By.CSS_SELECTOR, ".products img")
results_count = len(elm_veg_search_results)
print("Total results displayed count : "+str(results_count))
elm_addtocart_btns = driver.find_elements(By.XPATH, "//button[contains(text(),'ADD TO CART')]")
for elmbtn in elm_addtocart_btns:
    elmbtn.click()
print("Added all the results to Card for purchase")

elm_cart_btn = driver.find_element(By.XPATH, "// img[ @ alt = 'Cart']")
elm_cart_btn.click()
print("Clicked on 'Cart' button")

elm_proceed_to_checkout_btn = driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
elm_proceed_to_checkout_btn.click()
print("Clicked on 'Proceed to checkout' button")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promocode")))
elm_promocode_textbox = driver.find_element(By.CSS_SELECTOR, ".promocode")
elm_promocode_textbox.send_keys("rahulshettyacademy")
print("Entered 'rahulshettyacademy' in the coupon textbox")

elm_promocode_apply_btn = driver.find_element(By.CSS_SELECTOR, "button.promoBtn")
elm_promocode_apply_btn.click()
print("Clicked on 'Apply' coupon button")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

elm_promoinfo_msg = driver.find_element(By.CSS_SELECTOR, ".promoInfo")
print("Fetched the coupon info from the UI '" + elm_promoinfo_msg.text + "'")
assert elm_promoinfo_msg.text == "Code applied ..!"
print("Asserted coupon validation with the expected value and passed")

elm_placeorder_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
elm_placeorder_btn.click()
print("Clicked on the 'Place Order' button")

elm_choose_country_drpdown = driver.find_element(By.XPATH, "//label[contains(text(),'Choose Country')]/following::select")
drpdown_county = Select(elm_choose_country_drpdown)
drpdown_county.select_by_value("India")
print("Selected country as 'India' from dropdown")

elm_agree_checkbox = driver.find_element(By.CSS_SELECTOR, ".chkAgree")
elm_agree_checkbox.click()
assert elm_agree_checkbox.is_selected()
print("Selected agree terms and conditions checkbox and asserted successfully")

elm_proceed_btn = driver.find_element(By.XPATH, "//button[text()='Proceed']")
elm_proceed_btn.click()
print("Clicked on the 'Proceed' button")

# To validate the success message
elm_success_message = driver.find_element(By.XPATH, "//span[contains(text(),'Thank you')]")
assert "Thank you, your order has been placed successfully" in elm_success_message.text
print("purchase success!!!")

# To close the browser
driver.quit()
print(browserName + " browser closed successfully!!!")
