from GetBingPicture import GetBingPicture

if __name__ == '__main__':
    get_bing_picture = GetBingPicture()
    page_count = int(get_bing_picture.get_page_count())
    # print(page_count)
    current_page = 1
    while current_page <= page_count:
        print("page:", current_page)
        get_bing_picture.get_picture(current_page)
        current_page += 1
