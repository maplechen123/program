import requests

from bs4 import BeautifulSoup

# import xiaoshuoxiazai


url_list=[]

def get_html(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print('获取网页成功')
        return r.text
    except:
        return '获取网页失败'

def get_results(url):

    
    html=get_html(url)
    # print(html)
    soup=BeautifulSoup(html,'lxml')
    top_list=soup.find_all('div',class_='index_toplist mright mbottom')
    # print(top_list)
    for top in top_list:
        top_name=top.find('div',class_='toptab').find('span').text
        print(top_name)
        with open ('novel_list.txt','a+',encoding='utf-8') as f:
            f.write("\n小说种类：{} \n".format(top_name.ljust(30)))
        general_list=top.find(style='display: block;')
        book_list =general_list.find_all('li')

        for book in book_list:
            
            link = 'http://www.qu.la/' + book.a['href']
            # xiaoshuoxiazai.get_txt_url(link)
            title=book.a['title']
            url_list.append(link)
            with open('novel_list.txt','a+',encoding='utf-8')as f:
                f.write("小说名:{}小说地址:{}\n".format(title, link))

    return url_list


get_results('https://www.qu.la/paihangbang/')
