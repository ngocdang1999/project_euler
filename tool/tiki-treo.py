#!/usr/bin/python
# -*- coding: utf8 -*-
from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys

#x = "https://tiki.vn/gao-sach-gufoods-deo-mem-thom-1kg-p35957600.html?spid=35957601"
x = raw_input("Nhap URL: ")
n = raw_input ("Giay: ")
n = int(n)
browser = webdriver.Firefox()
browser.get("https://tiki.vn/")

time.sleep(10)
browser.find_element_by_id("onesignal-popover-cancel-button").click()

time.sleep(3)
browser.find_element_by_xpath(
    "/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/span/span").click()
time.sleep(3)
browser.find_element_by_xpath(
    "/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/div/button[1]").click()

time.sleep(10)
browser.find_element_by_id("email").send_keys("0949720907")
browser.find_element_by_id("password").send_keys("27061999")
browser.find_element_by_xpath(
    "/html/body/div[7]/div/div/div/div[2]/div[2]/form/div[3]/button[1]").click()

# Open new tab
time.sleep(3)
body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

# Load a page
browser.get(x)

time.sleep(1)
for i in range(1, 100000):
    c = browser.find_element_by_id("span-price").text
    c = c[:-2]
    c = int(c)
    print("Gia:", c,)
    print("Lan Thu :", i)
    e = "Sản phẩm đã hết hàng".decode('utf-8')
    if (browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/p[1]").text) == e:
            browser.refresh()
            time.sleep(1)
            print("Thoi gian Reload:", datetime.now().strftime("%H:%M:%S"))
    elif(c<21):
#Set so luong
        time.sleep(n)
        #browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").clear()
        #browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[2]/p[2]/div/input").send_keys(2)
        browser.find_element_by_xpath(
            "/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/button/span").click()
#Gio hang
        time.sleep(n)
        browser.find_element_by_xpath(
            "/html/body/header/div[2]/div/div[2]/div[3]/a/div/button").click()

        time.sleep(n)
        browser.find_element_by_xpath(
            "/html/body/div[10]/div/div[3]/div[4]/div/div[1]/button").click()
#Dia chi
        time.sleep(n)
       # browser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[4]/div/div/p[5]/button[1]").click()

        browser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[2]/div/div/p[5]/button[1]").click()

#Thuanbrowser.find_element_by_xpath("/html/body/div[4]/div/div/form/div[2]/div[5]/div/div/p[5]/button[1]").click()

        time.sleep(n)
        browser.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/form/div[9]/div/button").click()
        print("Thoi gian mua thanh cong:",
            datetime.now().strftime("%H:%M:%S"))
        browser.get(x)
    else:
        browser.refresh()
        time.sleep(1)
