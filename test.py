import requests
from bs4 import BeautifulSoup as bs

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url, headers = headers)
res.raise_for_status() # 200이면 코드 계속실행, 200이아니면 에러를 내고 멈춤
print("웹 스크래핑을 실시합니다.")

soup = bs(res.text,"lxml")
cartoons = soup.find_all("a", attrs={"class" : "title"}) # 해당 하는 모든 정보를 list형태로 가져와 줌.

for cartoon in cartoons:
    url_2 = "https://comic.naver.com"+cartoon["href"] # 2번째 url 주소이다.

    res_2 = requests.get(url_2) # 2번째 requests를 받을 객체이다.
    res_2.raise_for_status() # 200이면 코드 계속실행, 200이아니면 에러를 내고 멈춤

    soup_2 = bs(res_2.text,"lxml") # soup_2로 안의 웹사이트를 크롤링 한다.
    print(soup_2.find("span", attrs={"class" : "title"}).text.strip())
    print(soup_2.find("span", attrs={"class" : "wrt_nm"}).text.strip())
    print()
    ####