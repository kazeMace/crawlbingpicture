import requests
from bs4 import BeautifulSoup
from ConnectionDataBase import ConnectionDataBase
import GetUserAgent
import setting
import time
BASE_URL = setting.BASE_URL
HEADERS = setting.HEADERS
PARAMS = setting.PARAMS
USERAGENT = GetUserAgent.get_useragent()
HEADERS['user-agent'] = USERAGENT
class GetBingPicture:
    def __init__(self):
        self.session = requests.Session()
        self.session.get(url=BASE_URL)
    def get_page_count(self):
        req = self.session.get(url=BASE_URL, headers=HEADERS)
        html = BeautifulSoup(req.text, 'html5lib')
        page_count = html.select("body > div.page > span")[0].text.split("/")[1].strip()
        return page_count

    def get_picture(self, page):
        PARAMS['p'] = page
        print("page", page)
        req = self.session.get(url=BASE_URL, headers=HEADERS, params=PARAMS)

        html = BeautifulSoup(req.text, "html5lib")
        description_list = html.select("body > div.container > div > div > div.description > h3")
        date_list = html.select("body > div.container > div > div > div.description > p.calendar > em")
        location_list = html.select("body > div.container > div > div > div.description > p.location > em")
        picture_url_list = html.select("body > div.container > div > div > div.options > a.ctrl.download")
        middle_pic_url_list = html.select("body > div.container > div > div > img")
        small_pic_url_list = html.select("body > div.container > div > div > img")
        detail_page_url_list = html.select("body > div.container > div > div > a")
        item_dict = {}

        for i in range(len(description_list)):
            try:
                item_dict['description'] = description_list[i].text
            except Exception as e:
                item_dict['description'] = ""
            try:
                item_dict['location'] = location_list[i].text
            except Exception as e:
                item_dict['location'] = ""
            try:
                item_dict['date'] = date_list[i].text
            except Exception as e:
                item_dict['date'] = ""
            item_dict['picture_url'] = BASE_URL+picture_url_list[i].get("href")
            item_dict['middle_pic'] = middle_pic_url_list[i].get("data-progressive")
            item_dict['small_pic'] = small_pic_url_list[i].get("src")
            item_dict['detail_page_url'] = detail_page_url_list[i].get("href")
            print(item_dict)
            mongodb = ConnectionDataBase()
            mongodb.add(item_dict)
        time.sleep(5)


