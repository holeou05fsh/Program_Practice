from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import os
#%%------------------------------登入雲端救星------------------------------
driver = webdriver.Chrome('C:/pythondrive/chromedriver.exe')
driver.get('https://cloud.rookiesavior.net/')
driver.find_element_by_name('Account').send_keys("") #輸入帳號
driver.find_element_by_name('Password').send_keys("\n") #輸入密碼(\n不要刪掉)
time.sleep(0.8)
# driver.find_element_by_link_text('我知道了').click()
#%%------------------------------全部課程URL------------------------------
driver.execute_script("window.open('https://cloud.rookiesavior.net/Courses')")
driver.switch_to.window(driver.window_handles[1])
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
class_urls_check = soup.select('div.pagination-wrapper a')
# print(class_urls_check)
driver.close()
p = 0
class_urls =[]
for class_url_check in class_urls_check:
    driver.switch_to.window(driver.window_handles[0])
    class_url_plus = 'https://cloud.rookiesavior.net' + str(class_url_check['href'])
    # print(class_url_plus)
    driver.execute_script(f"window.open('{class_url_plus}')")
    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    class_urls.extend(soup.select('div.list-item a'))
    driver.close()
    p += 1
#%%------------------------------建立資料夾------------------------------
if not os.path.isdir('聯成雲端課'):
    os.mkdir('聯成雲端課')
driver.switch_to.window(driver.window_handles[0])
# print(class_urls[0])
#%%------------------------------建立課程資料夾------------------------------
for class_url in set(class_urls):
    a = 'https://cloud.rookiesavior.net' + str(class_url['href'])
    driver.execute_script(f"window.open('{a}')")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    chapter_html = driver.page_source
    soup_chapter = BeautifulSoup(chapter_html, 'html.parser')
    teacher = soup_chapter.find_all('div',{'class':'info-content'})
    class_name = soup_chapter.find('div',{'class':'course-main-title'}).text +'#'+teacher[4].text +'老師'
    class_name = class_name.replace('/', '_')
    class_name = class_name.replace('?', '')
    if not os.path.isdir(os.path.join('聯成雲端課', class_name)):
        os.mkdir(os.path.join('聯成雲端課', class_name))
#%%------------------------------建立課程資訊文件------------------------------
    Course_Information = soup_chapter.find_all('div',{'class':'course-info'})
    Course_Infortxt = os.path.join('聯成雲端課',class_name,'課程資訊.txt')
    with open(Course_Infortxt,'w',encoding='utf-8') as fp:
        fp.write(soup_chapter.find('div',{'class':'course-main-title'}).text)
        for i in Course_Information:
            fp.write(i.text)
        
#%%------------------------------建立章節資料夾------------------------------

    chapter_names = [names.text for names in soup_chapter.find_all('a', {"class": "panel-title"})]
    chapter_names = [re.sub('[<>\/|:*?]', '', name) for name in chapter_names]
    # print(chapter_names)

    for chapter_name in chapter_names:
        if not os.path.isdir(os.path.join('聯成雲端課', class_name, chapter_name)):
            os.mkdir(os.path.join('聯成雲端課', class_name, chapter_name))
    # print(chapter_html)
#%%------------------------------建立單元文件------------------------------
    chapter_units = re.findall('單元\d\\：\w+\W?\w+|尚無課綱', str(soup_chapter))
    # print(chapter_units)
    f = 0
    g = 0
    chapter_units.append("單元1")
    chapter_units.insert(0," ")
    chapter_names.insert(0,"123")
    y = [z for z in chapter_units if '元1' in z or '尚無' in z]
    for i in y:
        if chapter_units.index(i)==0:
            cript_dir = os.path.join('聯成雲端課',class_name,chapter_names[f],chapter_names[f]+'.txt')
            if os.path.exists(os.path.join('聯成雲端課',class_name,chapter_names[f])):
                with open(cript_dir,'w+',encoding='utf-8') as fp:
                    for j in range(chapter_units.index(i)+1):
                        fp.write(chapter_units[:chapter_units.index(i)+1][g]+'\n')
                        g += 1
                del chapter_units[:chapter_units.index(i)+1]
        else:

            cript_dir = os.path.join('聯成雲端課',class_name,chapter_names[f],chapter_names[f]+'.txt')
            if os.path.exists(os.path.join('聯成雲端課',class_name,chapter_names[f])):
                with open(cript_dir,'w+',encoding='utf-8') as fp:
                    for j in range(chapter_units.index(i)):
                        fp.write(chapter_units[:chapter_units.index(i)][g]+'\n')
                        g += 1
                del chapter_units[:chapter_units.index(i)]
        f += 1
        g = 0
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
#%%---------------------------------結束---------------------------------
driver.quit()