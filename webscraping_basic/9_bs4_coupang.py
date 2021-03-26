import requests 
import re
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=32&p=1"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("div", attrs={"class":re.compile("^box__component box__component-itemcard box__component-itemcard--general")})

#print(items[0].find("span", attrs={"class":"text__item"}).get_text())