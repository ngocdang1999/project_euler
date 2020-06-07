from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import time
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

x = raw_input("Enter the URL: ")

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
browser.maximize_window()
browser.get(x)

#Click "DA CO ID SENDO"

time.sleep(10)
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/form/div[1]/div/a[1]").click()

#Login ID Sendo

#time.sleep(30)
browser.find_element_by_id("log_username").send_keys("0898989523")
browser.find_element_by_id("log_password").send_keys("27061999Dang")
browser.find_element_by_id("login_real").click()

#Mua Hang
time.sleep(5)
for i in range(10000):
        #time.sleep(1)
        c = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/strong").text
        c = c[:-9]
        c = int(c)
        print("Gia:", c)
        print("Lan thu:", i)
        print("Thoi gian mua loi:", datetime.now().strftime("%H:%M:%S"))

        if c == 10:
            time.sleep(6)
            browser.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div[2]/div[4]/div/div/div/button/span").click()
            print("Mua thanh cong")
            print("Thoi gian mua thanh cong:", datetime.now().strftime("%H:%M:%S"))
            break
        else:
            browser.refresh()
            time.sleep(2)
