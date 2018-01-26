'''
抓取百度贴吧---郑州吧基本内容
爬虫线路： requests - bs4
Python版本： 3.6
OS： window7
'''


import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        # print (r.text)
        return r.text

    except:
        return '网页获取失败'

def gen_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''

    # 初始化一个列表来保存所有的帖子信息：
    contents=[]
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)
    # 我们来做一锅汤
    soup =BeautifulSoup(html,'lxml')
    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    li_tags=[]
    li_tags=soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
    # 通过循环找到每个帖子里的我们需要的信息：
    for li in li_tags:
        # 初始化一个字典来存储文章信息
        comment={}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        
        # 开始筛选信息，并保存到字典中
        try:
        # .split()是吧空格分开为不同的列表,strip()方法用于移除字符串头尾指定的字符(默认为空格)
            comment['title']=li.find('a').text.strip()
            comment['link']='http://tieba.baidu.com'+li.find('a')['href']
            comment['name']=li.find('span',attrs={'class':'tb_icon_author'}).text.strip()
            comment['time']=li.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
            comment['replynum']=li.find('span',attrs={'class':'threadlist_rep_num center_text'}).text.strip()
            contents.append(comment)

            # print(comment['title'])
            # print(comment['link'])
            # print(comment['name'])
            # print(comment['time'])
            # print(comment['replynum'])
        except:
            print('出了点小问题')
    # print(contents)
    #print(type(contents))
    return contents



def outfile(list):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''

    with open('tieba_spider.txt','a+',encoding='utf-8')as f:
        for l in list:
            f.write('标题: {}\t 链接: {}\t 发帖人: {}\t 发帖时间: {}\t 回复数量: {}\n'.format(
                    l['title'],l['link'],l['name'],l['time'],l['replynum']))
        print('爬虫保存完毕')

def main(base_url,pagenum):
    url_list=[]
    # 将所有需要爬去的url存入列表
    for i in range(0,pagenum):
        url_list.append(base_url+'&pn='+str(i*50))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据

    for url in url_list:
        outfile(gen_content(url))
        print('页面{}保存完毕'.format(url))

    print('所有的信息都已经保存完毕！')



# 设置需要爬取的基础页面
base_url='http://tieba.baidu.com/f?kw=郑州&ie=utf-8'
# 设置需要爬取的页码数量
pagenum=3

#当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':

    main(base_url, pagenum)

'''
小明.py
朋友眼中你是小明(__name__ == '小明'), 
你自己眼中你是你自己(__name__ == '__main__'), 
你编程很好, 朋友调你去帮他写程序(import 小明, 这时你在朋友眼中: __name__ == '小明'),
但你晚上也会打开xx网站, 做一些自己的事情(直接运行小明.py, __name__ == '__main__')

作者：铭尚hkyue
链接：https://www.zhihu.com/question/49136398/answer/138164069
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''