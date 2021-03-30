from selenium import webdriver
import time
import random

browser = webdriver.Chrome() #"./chromedriver.exe"
browser.get("http://www.naver.com")

browser.find_element_by_xpath("//*[@id='account']/a").click()

input_js = ' \
        document.getElementById("id").value="{id}"; \
        document.getElementById("pw").value="{pw}"; \
    '.format(id="test_id", pw="test_pw")

time.sleep(random.uniform(1,3))
browser.execute_script(input_js)
time.sleep(random.uniform(1,3))

browser.find_element_by_xpath("//*[@id='log.login']").click()