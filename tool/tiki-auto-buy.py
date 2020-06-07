from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
import time
from datetime import datetime

x = raw_input("Enter the URL: ")
#x = "https://tiki.vn/gao-sach-gufoods-deo-mem-thom-1kg-p35957600.html?spid=35957601"
#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.maximize_window()
#browser.set_window_size(1080, 800)
browser.get(x)


time.sleep(10)
browser.find_element_by_id(
    "onesignal-popover-cancel-button").click()

#browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").clear()
#browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").send_keys(2)
browser.find_element_by_xpath(
    "/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/button/span").click()
time.sleep(2)
browser.find_element_by_xpath(
    "/html/body/header/div[2]/div/div[2]/div[3]/a/div/button").click()
time.sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[10]/div/div[3]/div[4]/div/div[1]/button").click()

#Dang nhap
time.sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[1]/input").send_keys("0949720907")
browser.find_element_by_xpath(
    "/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[2]/input").send_keys("27061999")
browser.find_element_by_xpath(
    "/html/body/div[4]/div/div/div[2]/div/div/div[1]/form/div[5]/button").click()

#Dia chi
time.sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[4]/div/div/form/div[2]/div[4]/div/div/p[5]/button[1]").click()

#Hienbrowser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[2]/div/div/p[5]/button[1]").click()

#Thuanbrowser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[5]/div/div/p[5]/button[1]").click()
#Gia hang hoa
time.sleep(3)
for i in range(1, 10000):
    Gia = browser.find_element_by_xpath(
        "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/p[2]/span").text
    Gia = Gia[:-5]
    Gia = int(Gia)
    print("Gia:", Gia)
    print("Lan Thu:", i)

    if Gia < 21:
        browser.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/form/div[9]/div/button").click()
        print("Mua Thanh Cong", datetime.now().strftime("%H:%M:%S"))
        break
    else:
        browser.refresh()
        time.sleep(0.5)
        print("Thoi gian mua loi:", datetime.now().strftime("%H:%M:%S"))
