import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


single = 'なります'
url = 'https://cjjc.weblio.jp/sentence/content/' + quote(single)
req = requests.get(url).text
soup = BeautifulSoup(req,'html.parser')

single_find = re.compile('\w+、\w+'+single+'\w*?[？！。]?|\w+'+single+'?\w*?[？！。]?')
sentence = soup.select('div.qotC')
sentence_count_html = soup.select('p.qotHTR')
# print(page_count)
check = soup.find('div',{'id':'nrCntTH'}).text

#還未改
if '見つかりません' in check:
    print('single:'+single,' 見つかりません')
else:
    page_count = round(int(re.search('\d+',sentence_count_html[0].text).group(0))/49)
    sentence_count = re.search('\d+',sentence_count_html[0].text).group(0)
    if int(page_count) > 2:
        for j in range(page_count):
            req = requests.get(url+'/'+str(j+1)).text
            # print(url+'/'+str(j+1))
            soup = BeautifulSoup(req,'html.parser')
            sentence = soup.select('div.qotC')
            single_sentence = []
            for i in sentence:
                if len(single_sentence) < 10:
                    a = str(single_find.findall(i.text))
                    # print(a)
                    if len(a[2:-2]) > 14:
                        single_sentence.append(a[2:-2])
                # print(len(single_sentence))
            if len(single_sentence) > 10:
                break
    else:
        single_sentence = []
        for i in sentence:
            if len(single_sentence) < 10:
                a = str(single_find.findall(i.text))
                if len(a[2:-2]) > 1:
                    single_sentence.append(a[2:-2])
    
    
    sentence_list = []
    sentence_list.append(single_sentence)
# print(sentence_list)    
