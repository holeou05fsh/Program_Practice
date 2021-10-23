import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

with open('ます型二題以上(總和).json','r') as fp:
    a = json.load(fp)
    
dict_list = [i for i in a.keys()]


for i in dict_list:
    for j in range(len(a[i])):
        try:
            que = a[i][j]
            # print(count)
            url = 'https://cjjc.weblio.jp/sentence/content/' + quote(que)
            req = requests.get(url).text
            soup = BeautifulSoup(req,'html.parser')
            # print(soup)
            word = soup.find('p', {'class':'qotCJC'})
            # print(word)
            for k in word:
                # print(i)
                a[i][j] = {que:k}
                break
        except:
            continue
    # print(a[i])
    print("共"+str(len(dict_list))+'個', '目前'+str(dict_list.index(i)+1)+'個')

with open('ます型二題以上(總和)(含翻譯).json', 'w') as fp:
    json.dump(a, fp)
    
#%%  確認是否都對
with open('ます型二題以上(總和)(含翻譯).json','r') as fp:
    a = json.load(fp)
    
# with open('ます型二題以上(總和)(含翻譯).txt','w',encoding = 'utf-8') as fp:
    # fp.write(str(a))
    
li = [i for i in a.keys()]

# a['します'][2] = {'お詫びいたします。':'非常抱歉。'}
# a['します'][4] = {'乾杯をいたします。':'干杯。'}
# a['します'][8] = {'彼は明日出社します。':'他明天上班。'}
# a['実行します'][2] = {'プロジェクトＡを実行します。':'实施计划A。'}
# print(a['します'])


for i in li:
    for j in range(len(a[i])):
        if type(a[i][j]) != dict:
            print(i)
            print(a[i].index(a[i][j]), a[i][j])


# with open('ます型二題以上(總和)(含翻譯).json','w') as fp:
#     json.dump(a, fp)