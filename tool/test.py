from datetime import datetime
import time
from selenium import webdriver
from pip._vendor.distlib.compat import raw_input
mua liên tục gì m

hóng dea lỗi thôi

hết hàng thì cho reload


#x = raw_input("Enter the URL: ")
#n = raw_input("Giay: ")
browser = webdriver.Chrome()
browser.get("https://tiki.vn/")
browser.maximize_window()

time.sleep(3)
browser.find_element_by_id("onesignal-popover-cancel-button").click()
time.sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/span/span").click()
browser.find_element_by_xpath(
    "/html/body/div[1]/div/header/div[3]/div/div[2]/div[2]/div/button[1]").click()

time.sleep(2)
browser.find_element_by_id("email").send_keys("0949720907")
browser.find_element_by_id("password").send_keys("27061999")
browser.find_element_by_xpath(
    "/html/body/div[7]/div/div/div/div[2]/div[2]/form/div[3]/button[1]").click()

time.sleep(2)
x = "https://tiki.vn/thau-tam-kuku-ku1068-70-x-42-x-23-cm-p142081.html"
#browser = webdriver.Firefox()
browser.get(x)
time.sleep(1)
for i in range(1, 100):
    c = browser.find_element_by_id("span-price").text
    c = c[:-6]
    c = int(c)
    print("Gia:", c,)
    print("Lan Thu :", i)

    if (browser.find_element_by_xpath("/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/p[1]").text) == "Sản phẩm đã hết hàng":
        browser.refresh()
        time.sleep(1)
        print("Thời gian Reload:", datetime.now().strftime("%H:%M:%S"))
    elif(c == 327):
        browser.find_element_by_xpath(
            "/html/body/div[10]/div[2]/div[1]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/div[3]/button/span").click()
        time.sleep(1)
        browser.find_element_by_xpath(
            "/html/body/header/div[2]/div/div[2]/div[3]/a/div/button").click()
        time.sleep(1)
        browser.find_element_by_xpath(
            "/html/body/div[10]/div/div[3]/div[4]/div/div[1]/button").click()
        time.sleep(2)
        #ĐỊa Chỉ
        browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/form/div[2]/div[8]/div/div/p[5]/button[1]").click()
        time.sleep(1)
        browser.find_element_by_xpath(
            "/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/form/div[10]/div/button").click()
        browser.get(x)
    else:
        browser.refresh()
        time.sleep(1)
