import requests
res = requests.get("http://www.google.com")
res.raise_for_status()
#print("応答コード: ",res.status_code) # 200なら正常

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)