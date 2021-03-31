import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

#scroll
#browser.execute_script("window.scrollTo(0,1080)")
#browser.execute_script("window.scrollTo(0,2080)")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")

    if current_height == prev_height:
        break
    
    prev_height = current_height
print("scroll end")

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})

    if original_price:
        original_price = original_price.get_text() 
    else:
        # print(title, " <delete no discount movie>")
        continue
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).span.get_text()
    link = movie.find("div", attrs={"class":"b8cIId ReQCgd Q9MA7b"}).a["href"]
    link = "https://play.google.com" + link

    print(f"タイトル : {title}")
    print(f"値段 : {original_price}")
    print(f"割引値段 : {price}")
    print(f"リンク : {link}")
    print("-"*100)

browser.quit()