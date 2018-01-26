import bs4

soup =bs4.BeautifulSoup(open('Elsie.html'),'lxml')

print(soup.prettify())

print(soup.title)
print(type(soup.title))

print(soup.head)
print(soup.head.string)

head_tag=soup.head

print(head_tag.contents)

print(head_tag.children)

for child in head_tag.children:
    print(child)

for child in head_tag.descendants:
    print(child)

print(head_tag.string)

print(soup.strings)

for string in soup.strings:
    print(string)

