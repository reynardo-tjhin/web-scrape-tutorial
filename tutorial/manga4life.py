import requests

from bs4 import BeautifulSoup

# get the HTML document of the request
r = requests.get(url="https://manga4life.com/").content

# create a BeautifulSoup object
soup = BeautifulSoup(r, "html.parser")

# the website uses JavaScript to dynamically load content
# BeautifulSoup is excellent only in getting static html files
# to get dynamically loaded content, need to use libraries like Selenium
# Selenium needs web driver as it acts like a user going through the web browser
print(soup.find_all("div", class_="Chapter"))