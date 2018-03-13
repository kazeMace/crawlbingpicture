from fake_useragent import UserAgent
def get_useragent():
    ua = UserAgent()
    return ua.random