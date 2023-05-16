from bs4 import BeautifulSoup
import requests  # http 요청 처리 library

header = {
    "User-Agent": "Dongyang Mirae Univ"
}

# 뉴스
webPage1 = requests.get(
    "https://n.news.naver.com/article/586/0000057726",
    headers=header)
webPage2 = requests.get(
    "https://n.news.naver.com/article/277/0005259675",
    headers=header)

print(webPage1)

soup1 = BeautifulSoup(webPage1.content, "html.parser")  # html 형태로 파싱
print(soup1)
soup2 = BeautifulSoup(webPage2.content, "html.parser") 
print(soup2)

news1 = soup1.select_one("#dic_area").get_text().strip()  # 본문(글)이 있는 태그를 찾아 출력
print(news1)
news2 = soup2.select_one("#dic_area").get_text().strip() 
print(news2)
