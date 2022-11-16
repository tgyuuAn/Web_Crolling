import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url, headers = headers)
res.raise_for_status() # 200이면 코드 계속실행, 200이아니면 에러를 내고 멈춤
print("웹 스크래핑을 실시합니다.")

soup = bs(res.text,"lxml")
cartoons = soup.find_all("a", attrs={"class" : "title"}) # 해당 하는 모든 정보를 list형태로 가져와 줌.

data = ""
for cartoon in cartoons:
    data += cartoon.text+"\n"

with open("cartoons.txt","w",encoding = "utf-8") as f:
    f.write(data)