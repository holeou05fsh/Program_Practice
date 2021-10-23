from selenium import webdriver
from bs4 import BeautifulSoup
import time
from urllib.request import quote
import json
import os

with open('ます型二題以上(總和).json', 'r') as fp:
    a = json.load(fp)
single_list = [i for i in a.keys()]

f = os.listdir('D:\OneDrive\桌面\日語單字\ます型二題以上(總和)(意思)')
f = [i.replace('.txt','') for i in f]

for single in single_list:
    try:
        if single not in f:
            driver = webdriver.Chrome('C:/pythondrive/chromedriver.exe')
            driver.get('https://dict.hjenglish.com/jp/jc/'+quote(single))
            time.sleep(1)
            driver.find_element_by_xpath("//button[contains(text(),'日 → 中')]").click()
            time.sleep(2)
            html = driver.page_source
            url_check = driver.current_url
            driver.quit()
            
            if 'notfound' not in url_check:
                soup = BeautifulSoup(html, 'html.parser')
                data = soup.find('header',{'class':'word-details-pane-header'})
                info = data.text
                
                li = info.split('\n')
                li = [i+'\n' for i in li if i != '']
                li = [i.replace(']\n', ']') for i in li]
                
                with open('ます型二題以上(總和)(意思)/'+single+'.txt', 'w', encoding='utf-8') as fp:
                    for i in li:
                        fp.write(i)
            else:
                print(single)
                continue
        else:
            continue
    except:
        print(single)
        print(single_list.index(single))
        exit()