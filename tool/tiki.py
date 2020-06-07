from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import time
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.options import Options

x=raw_input("Enter the URL: ")
n=raw_input("Enter the number of seconds: ")
n=int(n)

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
browser.maximize_window()
browser.get(x)

time.sleep(n)
print(browser.title)
print(browser.current_url)

time.sleep(n)
browser.find_element_by_id("onesignal-popover-cancel-button").click()
time.sleep(n)
#browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").clear()
#browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").send_keys(2)
browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/button/span").click()


time.sleep(n)
browser.find_element_by_xpath("/html/body/header/div[2]/div/div[2]/div[3]/a/div/button").click()

time.sleep(n)
browser.find_element_by_xpath("/html/body/div[10]/div/div[3]/div[4]/div/div[1]/button").click()

time.sleep(n)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[1]/input").send_keys("0949720907")
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[2]/input").send_keys("27061999")
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[5]/button").click()

time.sleep(n)
browser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[8]/div/div/p[5]/button[1]").click()


time.sleep(10)
gia = browser.find_elements_by_css_selector("total2")
for gia in gia:
    print(gia.text)

time.sleep(n)
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/form/div[9]/div/button").click()
#browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/span/span").click()
#browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/div/button[1]").click()

