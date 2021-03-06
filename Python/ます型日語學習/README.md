# ます型日語學習-Python

## 📢　前言：

網路很少對於日語單字型態，做出學習及題目的網站或程式，所以就嘗試著製作。
日語當中ます型是第二類動詞變化，丁寧形表示禮貌用法。

## 🛠　項目使用技術：

* 爬蟲工具：requests、selenuim
* 網頁解析工具：beautifulsoup、re
* 文件格式：Json、txt
* 音檔撥放工具：tempfile、gtts、pygame
* GUI工具：tkinter
* 生成執行檔工具：pyinstaller

## 🛠　程式過程概述：
* 利用爬蟲工具至日語網站爬取單字、例句、翻譯、單字意思。
* 將單字、句子、翻譯製作成Json檔，以及單字意思製作成txt檔。
* 使用random再Json檔中隨機產生出題目出來。
* 把隨機值對應在句子內的單字取代挖空，做成題目及答案。
* 利用tempfile產生臨時文件，用gtts生成音檔丟入臨時文件中，在用pygame執行音檔。
* 用tkinter製作整的日語學習用的介面
* 最後用pyinstaller打包成exe執行檔

## 📝　程式過程展示：

![1](https://user-images.githubusercontent.com/79140074/142711257-26f1e934-58e0-4dcb-acf8-a14098da3ad5.png)

在OJAD網站中爬取單字，爬200頁的單字(約3594個單字)，爬出單字有其他型態，用正則表達式(regex)，把ます型給取出
****
![2](https://user-images.githubusercontent.com/79140074/142711624-810518b0-b080-4392-8e00-9b5786601c62.png)

用ます型單字，再weblio網站爬句子
****
![3](https://user-images.githubusercontent.com/79140074/142711262-cf497027-8d7e-40a2-bd52-fb22853d55a5.png)

用單字爬意思，用selenium在沪江小D網站爬單字意思。
****

## 🧑‍🎓　程式展示：
![11](https://user-images.githubusercontent.com/79140074/142711263-1686582e-c135-4998-ad72-757bf538a5a9.png)

****
![12](https://user-images.githubusercontent.com/79140074/142711585-3d4c71ed-ead1-42d9-bef9-6de3175aae8b.png)

****
![13](https://user-images.githubusercontent.com/79140074/142711265-bee974d0-a8ac-4547-9d26-fa88f2900433.png)

## 📝　爬蟲網站：

http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/category:verb/order:name

OJAD - Offene Jugendarbeit Dornbirn

https://cjjc.weblio.jp/category/wchnt/z/32

Weblio辞書

https://dict.hjenglish.com/jp/

沪江小D日语词典
