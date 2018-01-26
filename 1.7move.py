import gethtml
import pprint
import requests

move1=[]


def get_contents(url):
    
    soup=gethtml.get_html(url)
    pic_list=soup.find_all('img')
    for pic in pic_list:
        picurl='http:'+pic['src']
        picname=pic['title']
        get_pic(picurl,picname)
    move_temp=soup.find_all('div',class_='txt')
    for move in move_temp:
        move_list={}
        move_actor=[]
        actor_list=move.find_all('p',class_='pActor')
        for actor in actor_list:
            actor_temp=actor.find_all('a')
            
            for actor in actor_temp:
                move_actor.append(actor.text)
        move_list['电影名称']=move.find('a').text
        move_list['主演']=move_actor
        info=move.find('p',class_='pTxt pIntroShow').text

        if '展开全部' in info:
            move_list['简介']=move.find('p',class_='pTxt pIntroHide').text[3:-7]
        else:
            move_list['简介']=info
        
        move1.append(move_list)
    pprint.pprint(move1)
        
def get_pic(url,filename):
    pic_content = requests.get(url).content
    with open('E:/python/spider/img/'+filename+'.jpg','wb') as f:
        f.write(pic_content)
        
    
    





get_contents('http://dianying.2345.com/top/')


