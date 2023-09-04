import requests
import NewsBot
import json


server_url = "http://52.79.53.117/api/news/bot/"


def make_json():
    with open('keywords.txt', 'r') as keywords_file:
        keywords = keywords_file.read().split()

    data = dict()
    for keyword in keywords:
        news_naver = NewsBot.NaverNews(keyword)
        news_google = NewsBot.GoogleNews(keyword)
        for elem in news_naver+news_google:
            data[len(data)] = elem

    return json.dumps(data, indent=4, ensure_ascii=False).encode("utf-8")


def json_to_server(json_data):

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(server_url, data=json_data, headers=headers)

    if response.status_code == 201:
        print("JSON data successfully sent to the server.")
    else:
        print("Server Connetion Error")


if __name__ == '__main__':
    json_data = make_json()
    print(json_data)

    json_to_server(json_data)
