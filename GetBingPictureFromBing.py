import requests
from bs4 import BeautifulSoup
from ConnectionDataBase import ConnectionDataBase
import GetUserAgent
import setting
import time
BASE_URL = setting.BASE_URL
BING_URL = setting.BING_URL
HEADERS = setting.HEADERS
PARAMS = setting.PARAMS
USERAGENT = GetUserAgent.get_useragent()
HEADERS['user-agent'] = USERAGENT
class GetBingPicture:
    def __init__(self):
        self.session = requests.Session()
        self.session.get(url=BING_URL, headers=HEADERS)

    def get_picture(self):
        req = self.session.get(url=BING_URL, headers=HEADERS)
        html = BeautifulSoup(req.text, 'html5lib')
        picture_url = html.select("#bgDiv")[0]

        print(picture_url)

g =GetBingPicture()
g.get_picture()