from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# Here are some simple ways to navigate that data structure

# <title>The Dormouse's story</title>
print(soup.title) 

# u'title'
print(soup.title.name)

# u'The Dormouse's story'
print(soup.title.string)

# u'head'
print(soup.title.parent.name)

# <p class="title"><b>The Dormouse's story</b></p>
print(soup.p)

# u'title'
print(soup.p['class'])

# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.a)

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find_all('a'))

# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
print(soup.find(id="link3"))

# one common task is extracting all the URLs found within a page's <a> tags:
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
for link in soup.find_all('a'):
    print(link.get('href'))

# another common task is extracting all the text from a page:
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...
print(soup.get_text())