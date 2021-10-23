import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json

# with open('ます型單字(11字).txt', 'r', encoding='utf-8') as fp:
#     wordtolist = fp.read().splitlines()
wordtolist = ['なります']
# print(nine_word)
sentence_list = []
sentence_dic = {}
for i in wordtolist:
    single = i
    url = 'https://cjjc.weblio.jp/sentence/content/' + quote(single)
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    single_find = re.compile('\w+、\w+' + single + '\w*[？！。]?|\w+' + single + '\w*[？！。]?|' + single + '\w*[？！。]?')
    sentence = soup.select('p.qotCJJ')
    sentence_count_html = soup.select('p.qotHTR')
    # print(page_count)
    check = soup.find('div', {'id': 'nrCntTH'})
    # print(check)
    if check != None:
        single_sentence = []
        sentence_list.append([])
        print('single:' + single, ' 見つかりません')
    else:
        stop = 0
        page_count = round(int(re.search('\d+', sentence_count_html[0].text).group(0)) / 49)
        sentence_count = re.search('\d+', sentence_count_html[0].text).group(0)
        single_sentence = []
        if int(page_count) > 2:
            for j in range(page_count):
                # print(j)
                req = requests.get(url + '/' + str(j + 1)).text
                # print(url+'/'+str(j+1))
                soup = BeautifulSoup(req, 'html.parser')
                sentence = soup.select('p.qotCJJ')

                for i in sentence:
                    if len(single_sentence) < 10:
                        a = str(single_find.findall(i.text))

                        if len(a[2:-2]) > 8:
                            single_sentence.append(a[2:-2])
                    else:
                        stop = 1
                        break
                if stop == 1:
                    break
        else:
            single_sentence = []
            for i in sentence:
                if len(single_sentence) < 10:
                    a = str(single_find.findall(i.text))
                    if len(a[2:-2]) > 1:
                        single_sentence.append(a[2:-2])

        # sentence_list.append(single_sentence)
        sentence_dic[single] = single_sentence
    print(single, str(len(single_sentence)) + '題')
print(sentence_dic)

# with open('ます型題目(11字).json', 'w', encoding='utf-8') as fp:
#     json.dump(sentence_dic, fp)




