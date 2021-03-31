import requests
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.daum.net/"
browser.get(url)

keyword = "송파 헬리오시티"

browser.find_element_by_id("q").send_keys(keyword)
browser.find_element_by_class_name("ico_pctop.btn_search").click()

res = requests.get(browser.current_url) 
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for index, row in enumerate(data_rows):
    columns = row.find_all("td")
    print("=========== 매물 {index} ============".format(index=index+1))
    print(f"거래 : {columns[0].get_text()}")
    print(f"면적 : {columns[1].get_text()} (공급/전용)")
    print(f"가격 : {columns[2].get_text()} (만원)")
    print(f"동 : {columns[3].get_text()}")
    print(f"층 : {columns[4].get_text()}")
browser.quit()