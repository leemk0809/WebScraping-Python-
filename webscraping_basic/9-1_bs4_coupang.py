import requests 
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

for i in range(1,6):
    #print("page : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={page}&rocketAll=false&searchIndexingToken=".format(page=i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        #広告物は外します。
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print("広告物は外します")
            continue
        name = item.find("div",attrs={"class":"name"}).get_text()
        # Appleの品物は外します。
        if "Apple" in name:
            #print("Appleの品物は外します。 ")
            continue
        price = item.find("strong", attrs={"class":"price-value"}).get_text()

        # review 400+, rating 4.5+だけ調べます
        rating = item.find("em", attrs={"class":"rating"})
        if rating:
            rating = rating.get_text()
        else:
            #print("評点ない品物は外します。")
            continue
        rating_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rating_cnt:
            rating_cnt = rating_cnt.get_text()[1:-1] #slicing
        else:
            #print("レビューがない品物は外します。")
            continue
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        if float(rating) >= 4.5 and int(rating_cnt) >= 400:
            #print(name, price, rating, rating_cnt)
            print(f"名前：{name}")
            print(f"値段：{price}")
            print(f"評点：{rating} (レビュー数：{rating_cnt})")
            print("link : https://www.coupang.com{link}".format(link=link))
            print("-"*100)
        
