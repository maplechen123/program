import requests

import bs4




def get_html(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print('获取网页成功')
        return r.text
    except:
        return '获取网页失败'

def get_txt_url(url):
    html=get_html(url)
    soup=bs4.BeautifulSoup(html,'lxml')
    text_name_list=soup.find_all('dd')
    print(type(text_name_list))
    #由于小说章节太多,只选择前两张实验
    for text_name in text_name_list[0:2]:
        print(text_name.a.string)
        link = 'https://www.qu.la'+text_name.a['href']
        print(link)
        #调用函数  下载小说
        get_txt(link,text_name.a.string)
#读取小说页面的正文,写入txt保存为名字为章节的txt文件
def get_txt(url,name):
    html =get_html(url).replace('<br/>', '\n')
    html=html.replace('&nbsp;','')
    soup=bs4.BeautifulSoup(html,'lxml')
    txt=soup.find('div',id='content')
    print(type(txt.text))
    print(txt.text)
    with open('{}.txt'.format(name),'a+',encoding='utf-8') as f:
        f.write(txt.text.replace('chaptererror();', ''))
        


get_txt_url('https://www.qu.la/book/32/')

