import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os

url ='https://www.ptt.cc/bbs/Beauty/index.html'
session = requests.session()
data = {'from': '/bbs/Beauty/index.html','yes': 'yes'}
reqse = session.post('https://www.ptt.cc/ask/over18',data=data)
req = session.get(url).text
re_img = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

if not os.path.isdir('Download_PTTpictures'):
    os.mkdir('Download_PTTpictures')

for i in range(2):
    req = session.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    articles = soup.select('div.title a')
    Previous_page_element = soup.select('div.btn-group-paging a')
    url = 'https://www.ptt.cc/' + Previous_page_element[1]['href']
    for article in  articles:
        try:
            article_name = article.text.replace('<','')
            if not os.path.isdir(os.path.join('Download_PTTpictures', article_name)):
                os.mkdir(os.path.join('Download_PTTpictures', article_name))
            # print(article['href'],article.text)
            page = session.get('https://www.ptt.cc/'+article['href']).text
            pictures = re.findall(re_img,page)
            re_img_name = re.compile('http[s]?://i.imgur.com/(\w+\.(?:jpg|png|gif))')
            pic_size = 0
            for picture in set(pictures):
                urlretrieve(picture,os.path.join('Download_PTTpictures',article.text,re_img_name.search(picture).group(1)))
                # print(re_img_name.search(picture).group(1))
                # a = os.path.getsize('D:/OneDrive/桌面/爬蟲練習/Download_PTTpictures/'+article.text+'/'+re_img_name.search(picture).group(1))
                a = os.path.getsize(os.path.join('Download_PTTpictures',article.text,re_img_name.search(picture).group(1)))
                pic_size += a
            if pic_size >= 1048576:
                file_size = '圖片%d個，共%.2f MB' % (len(set(pictures)),pic_size/1024/1024)
            else:
                file_size = '圖片%d個，共%d KB' % (len(set(pictures)),pic_size/1024)
            print(article.text,';',str(file_size),'(下載完)')
        except:
            pass