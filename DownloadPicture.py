import os
import re
import requests
from ConnectionDataBase import ConnectionDataBase
# BASE_PATH = "/bing_picture"
try:
    os.mkdir("bing_picture")
except Exception as e:
    print("文件夹已存在")

def download_picture():
    connextion = ConnectionDataBase()
    all_items = connextion.get_item()
    for item in all_items:
        picture_url = item["picture_url"]
        req = requests.get(picture_url, stream=True)
        picture_name = re.search("photo/(\w+-\w+)?", picture_url)[1]+".jpg"
        picture_path = "bing_picture/"+picture_name
        has_exsit = os.path.exists(picture_path)
        print(picture_name)
        if has_exsit == True:
            print("该文件已存在")
        else:
            with open(picture_path, 'wb') as file:
                file.write(req.content)
download_picture()