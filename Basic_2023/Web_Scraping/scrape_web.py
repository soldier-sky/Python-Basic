''' Example scraping website page. Using Y combinator as example
'''
import requests                         # required to downloads the HTML pages
from bs4 import BeautifulSoup           # To parse the html page and navigate
# Refer https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup for more details.

url='https://news.ycombinator.com/'
res = requests.get(url)

print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')

#print(soup.find_all('div'))
# print(soup.text)                  # prints all text in website
print(soup.title)