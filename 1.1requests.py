import requests
import random


r= requests.get("http://www.baidu.com")


#requests.get（）返回一个response对象
print(r)

#response.text 为源码文件
#print(r.text)

hd={'User-agent':'123'}


r= requests.get("http://www.baidu.com",headers=hd)


print('r.request.headers返回值:')
print(r.request.headers)
print()

print('r.status_code返回值:')
print(r.status_code)
print()

print('r.headers返回值:')
print(r.headers)
print()

print('r.encoding返回值:')
print(r.encoding)
print()

print('r.apparent_encoding返回值:')
print(r.apparent_encoding)
print()

# print('r.content返回值:')
# print(r.content)
# print()

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        # 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，
        # 我们可以通过 Response.raise_for_status() 来抛出异常：
        # 由于我们的例子中 r 的 status_code 是 200 ，
        # 当我们调用 raise_for_status() 时，得到的是：
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

l=getHtmlText('http://.ss.com')
print(l)