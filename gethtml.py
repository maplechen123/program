import requests

import bs4


def get_html(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='gbk'
        soup=bs4.BeautifulSoup(r.text,'lxml')
        print('获取网页soup成功')
        return soup
    except:
        return '获取网页失败'
