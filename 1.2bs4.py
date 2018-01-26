from bs4 import BeautifulSoup

html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</html>
'''

soup = BeautifulSoup(html,'html.parser')

print(soup.prettify())

#找到文档的title
print('soup.title返回值:')
print(soup.title)
print(type(soup.title))
print(soup.title.contents)
print()

#title的name值
print('soup.title.name返回值:')
print(soup.title.name)
print()

#title中的字符串String
print('soup.title.string返回值:')
print(soup.title.string)
print()

#title的父亲节点的name属性
print('soup.title.parent.name返回值:')
print(soup.title.parent.name)
print()

#文档的第一个找到的段落
print('soup.p返回值:')
print(soup.p)
print()

#找到的p的class属性值
print('soup.p[\'class\']返回值:')
print(soup.p['class'])
print()

#找到a标签第一个
print('soup.a返回值:')
print(soup.a)
print()

#找到a标签所有的
print('soup.find_all(\'a\')返回值:')
print(soup.find_all('a'))
print()

#找到id值等于3的a标签
print('soup.find(id=\'link3\')返回值:')
print(soup.find(id='link3'))
print()



for link in soup.find_all('a'):
    print(link)
    print(link.get('href'))

#我们可以通过get_text 方法 快速得到源文件中的所有text内容。
print(soup.get_text())
print(type(soup.get_text()))