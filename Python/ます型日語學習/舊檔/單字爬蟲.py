# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/search'
req = requests.get(url).content
# print(res)

soup = BeautifulSoup(req,'html.parser') 
singe = soup.select('div.midashi_wrapper')
findmasu = re.compile('・\w+')
for i in singe:
    with open('日語單字.txt','w',encoding='utf-8') as fp:
        for i in singe:
            findmasu_n = findmasu.findall(i.text)[0].replace('・','')
            fp.write(findmasu_n +'\n')
next_page = soup.select('span.next a')
# print(next_page[0]['href'])
next_page_url = 'http://www.gavo.t.u-tokyo.ac.jp' + next_page[0]['href']
# print(next_page_url)
for i in range(200):
    reqs = requests.get(next_page_url).content
    nsoup = BeautifulSoup(reqs,'html.parser')
    singes = nsoup.select('div.midashi_wrapper')
    with open('日語單字.txt','a',encoding='utf-8') as fp:
        for i in singes:
            try:
                findmasu_n = findmasu.findall(i.text)[0].replace('・','')
                fp.write(findmasu_n +'\n')
            except:
                pass
    next_page = nsoup.select('span.next a')
    next_page_url = 'http://www.gavo.t.u-tokyo.ac.jp' + next_page[0]['href']


    