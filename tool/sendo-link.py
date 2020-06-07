from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import time
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.options import Options

x = raw_input("Enter the URL: ")
#n = raw_input("Enter the number of seconds: ")
#n = int(n)

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
browser.maximize_window()
browser.get(x)


#browser = webdriver.Firefox()
#browser = webdriver.Chrome()
#browser.maximize_window()

#browser.get("https://www.sendo.vn/bo-dao-5-mon-cao-cap-sang-trong-tien-loi-19141879.html")


time.sleep(25)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/section[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/button[1]").click()


#browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/section[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/input").clear()
time.sleep(5)
#browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/section[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/input").send_keys(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/section[1]/div[2]/div[1]/div[2]/div[5]/div/div[2]/button[2]").click()

#Dang Nhap
time.sleep(25)
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/span").click()
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div/div[2]/form/div/div[1]/div/input").send_keys("0949720907")
browser.find_element_by_xpath(
    "/html/body/div[4]/div/div[1]/div/div/div/div[2]/form/div/div[2]/div/div/input").send_keys("270604081999")
browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div/div[2]/form/div/div[4]/div[2]/button").click()
#Mua Hang
time.sleep(30)
for i in range(10000):
    #time.sleep(1)
    c = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/strong").text
    c = c[:-5]
    c = int(c)
    print("Gia:",c)
    print("Lan thu:",i)

    if c < 10:
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[4]/div/div/div/button/span").click()
        print("Mua thanh cong")
        break
    else:
        browser.refresh()
        time.sleep(2)
