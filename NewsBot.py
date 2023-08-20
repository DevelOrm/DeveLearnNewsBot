import datetime
import requests
from urllib import parse
from bs4 import BeautifulSoup


curr_time = str(datetime.datetime.now())


def NaverNews(keyword):

    url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}'

    news_list = []
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.select("li.bx > div > div.news_area > a")
        for i in elements:
            title = i.attrs['title']
            link = i.attrs['href']
            news_list.append({'title': title, 'link': link, 'time': curr_time})
    else:
        print(response.status_code)

    return news_list


def GoogleNews(keyword):
    parsed_keyword = parse.quote(keyword)
    url = f'https://news.google.com/search?q={parsed_keyword}&hl=ko&gl=KR&ceid=KR%3Ako'

    news_list = []
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        elements = soup.select("div.xrnccd > article > h3 > a")
        for i in elements:
            title = i.getText()
            link = "https://news.google.com" + i.attrs['href'][1:]
            news_list.append({'title': title, 'link': link, 'time': curr_time})
    else:
        print(response.status_code)
    return news_list


if __name__ == "__main__":
    # news_navse = NaverNews("개발자취업")
    # for elem in news:
    #     print(f'title : {elem["title"]}')
    #     print(f'link : {elem["link"]}')
    #     print()
    news_google = GoogleNews("개발자취업")
    for elem in news_google:
        print(f'title : {elem["title"]}')
        print(f'link : {elem["link"]}')
        print()
