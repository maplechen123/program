'''
爬取Dota菠菜结果信息
使用 requests --- bs4 线路
Python版本： 3.6
'''

import requests
from bs4 import BeautifulSoup
import time

contents=[]

def get_html(url):
    try:
        r=requests.get(url,timeout=30)
        print('获取网页成功.....')
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print('获取网页成功')
        return r.text
    except:
        return '获取网页失败'

def get_contents(url):
    
    

    content=get_html(url)
    
    soup=BeautifulSoup(content,'lxml')
    match_list=soup.find_all('div',attrs={'class':'matchmain bisai_qukuai'})
    # print(match_list)
    for match in match_list:
        time=match.find('div',attrs={'class':'whenm'}).text.strip()
        teamname=match.find_all('span',attrs={'class':'team_name'})
        if teamname[0].string[0:3]=='php':
            teamname1_name='暂无队名'
        else:
            teamname1_name=teamname[0].string

        if teamname[1].string[0:3]=='php':
            teamname2_name='暂无队名'
        else:
            teamname2_name=teamname[1].string

        teamname1_point=match.find('span',class_='team_number_green').text
        teamname2_point=match.find('span',attrs={'class':'team_number_red'}).string
        print(time)
        print('队伍一:',teamname1_name,teamname1_point)
        print('队伍二:',teamname2_name,teamname1_point)

get_contents('http://dota2bocai.com/match')


