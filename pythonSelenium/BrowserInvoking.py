from selenium import webdriver

browserName = "Chrome"
if browserName.upper() == "CHROME":
    from selenium.webdriver.chrome.service import Service
    s = Service("/pythonSelenium/browserdrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
elif browserName.upper() == "FIREFOX":
    from selenium.webdriver.firefox.service import Service
    s = Service("/pythonSelenium/browserdrivers\\geckodriver.exe")
    driver = webdriver.Firefox(service=s)
elif browserName.upper() == "EDGE":
    from selenium.webdriver.edge.service import Service
    s = Service("/pythonSelenium/browserdrivers\\msedgedriver.exe")
    driver = webdriver.Edge(service=s)
else:
    print("Invalid Browser")

driver.implicitly_wait(60)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.service.path)
print(driver.service.port)
# driver.quit() -> To quit the browser
