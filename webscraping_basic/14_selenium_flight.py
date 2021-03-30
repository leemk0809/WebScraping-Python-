from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

browser.find_element_by_class_name("calendar-btn-next-mon.sp_flight").click()

browser.find_elements_by_link_text("27")[1].click()
browser.find_elements_by_link_text("28")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[5]").click()
browser.find_element_by_xpath("//*[@id='searchArea']/a").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()

