import requests
import NewsBot
import json


def make_json():
    with open('keywords.txt', 'r') as keywords_file:
        keywords = keywords_file.read().split()

    data = dict()
    for keyword in keywords:
        news_naver = NewsBot.NaverNews(keyword)
        news_google = NewsBot.GoogleNews(keyword)
        for elem in news_naver+news_google:
            data[len(data)] = elem

    return json.dumps(data, indent=4, ensure_ascii=False)


def json_to_server(json_data):

    url = "http://localhost:8000/api/data/"  # 서버 주소로 변경

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 201:
        print("JSON data successfully sent to the server.")
    else:
        print("Server Connetion Error")


'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class JSONDataView(APIView):
    def post(self, request, format=None):
        data = request.data
        return Response({'message': 'JSON data received successfully'}, status=status.HTTP_201_CREATED)
'''


if __name__ == '__main__':
    json_data = make_json()
    print(json_data)

    # json_to_server(json_data)
