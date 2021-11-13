# Django開發-食堂系統網站

## 📢　前言：

在之前服務業的工作中，有許多點餐、叫餐的工作要做，而此服務也在花費了許多時間，也會有許多的問題發生，例如叫錯餐、少餐、忙碌而延餐、記帳錯誤等問題，許多狀況發生，因而想寫以點餐為主的網站，此網站主要由2大應用，一、前臺系統：已員工於前臺網站進行客戶店餐作業系統，二、後臺系統：以管理員控管員工信息、店家資訊、菜品分類及資訊、會員訊息管理等 ; 主要以網站對於SQL進行增刪改查等操作。
    
## 🛠　項目使用技術：

* 使用Django框架，版本：2.2.*的LTS版本。
* MySQL數據庫。
* 連結數據庫：mysqlclient 2.0.3。
* 圖像處理： Pillow 8.4.0。
* Web前端技術：HTML、CSS、JavaScript和Jquery等。
* 前端代碼引用：https://github.com/ColorlibHQ/AdminLTE 、 www.xuebiancheng.cn

## 🎨　E-R圖 / 項目功能模塊圖：
<img src="https://user-images.githubusercontent.com/79140074/141459842-0e438da2-6ce2-49ba-b9b0-cf54216b12c3.png" width="420">   <img src="https://user-images.githubusercontent.com/79140074/141459845-ee948a55-e651-4f2b-8893-db9aae4a99f0.png" width="457">

## 📝　員工後臺管理應用：
網站後台模板採用github上提供的一個後台管理界面，

網址：https://github.com/ColorlibHQ/AdminLTE 、 https://github.com/alecfan/mstp_17_akira

<table>
  <tr>
    <td>模塊</td>
    <td>操作</td>
    <td>權限</td>
  </tr>
  <tr>
    <td>登錄&退出管理</td>
    <td>登錄界面、處理登錄、驗證碼、退出</td>
    <td>無</td>
  </tr>

  <tr>
    <td>後台首頁</td>
    <td>後台首頁</td>
    <td>管理員</td>
  </tr>
  <tr>
    <td>員工信息管理</td>
    <td>瀏覽(搜索&分頁)、執行添加、編輯、刪除(狀態修改)</td>
    <td>管理員</td>
  </tr>
  <tr>
    <td>店鋪信息管理</td>
    <td>瀏覽(搜索&分頁)、執行添加、編輯、刪除(狀態修改)</td>
    <td>管理員</td>
 </tr>
 <tr>
    <td>菜品類別管理</td>
    <td>瀏覽(搜索&分頁)、執行添加、編輯、刪除(狀態修改)、各菜品明細</td>
    <td>管理員</td>
 </tr>
 <tr>
    <td>菜品信息管理</td>
    <td>瀏覽(搜索&分頁)、執行添加、編輯、刪除(狀態修改)</td>
    <td>管理員</td>
 </tr>
 <tr>
    <td>會員信息管理</td>
    <td>瀏覽(搜索&分頁)、執行添加、編輯、刪除(狀態修改)</td>
    <td>管理員</td>
 </tr>
</table>



## 📝　食堂前臺管理應用：
網站前台模板採用網址：www.xuebiancheng.cn 網站課程。
<table>
  <tr>
    <td>模塊</td>
    <td>操作</td>
    <td>權限</td>
  </tr>
  <tr>
    <td>登錄&退出管理</td>
    <td>登錄界面、選擇店鋪、處理登錄、驗證碼、退出</td>
    <td>無</td>
  </tr>
 <tr>
    <td>店鋪中菜品類別與菜品展示</td>
    <td>菜品類別、菜品展示</td>
    <td>員工、管理員</td>
 </tr>
 <tr>
    <td>購物車(點餐)</td>
    <td>添加菜品、查看、修改、刪除、清空</td>
    <td>員工、管理員</td>
 </tr>
 <tr>
    <td>訂單處理</td>
    <td>訂單處理界面、訂單詳情、執行訂單處理</td>
    <td>員工、管理員</td>
 </tr>
 <tr>
    <td>歷史訂單管理</td>
    <td>查看歷史訂單、訂單詳情</td>
    <td>員工、管理員</td>
 </tr>
 <tr>
    <td>無效訂單管理</td>
    <td>查看無效訂單、訂單詳情</td>
    <td>員工、管理員</td>
 </tr>
</table>

## 📞　前後台網址：
http://主機名:端口/應用名/視圖名/函數名

* 前端登入：http://127.0.0.1:8000/login
* 前端首頁：http://127.0.0.1:8000/web/
* 後端登入：http://127.0.0.1:8000/myadmin/login
* 後端首頁：http://127.0.0.1:8000/myadmin/

## 📂　項目的目錄結構：
本次項目共計二個應用：myadmin(後臺)、web(前臺)

```` 
📂myweb/ 項目目錄
  |   
  |--📂myadmin/ 後台管理應用
  |    |--📂views/
  |    |    |--📄category.py 菜品分類管理視圖
  |    |    |--📄index.py 後台首頁、登錄、退出、驗證碼加載等視圖方法
  |    |    |--📄member.py 會員管理視圖
  |    |    |--📄product.py 菜品信息管理視圖
  |    |    |--📄shop.py 店鋪管理視圖
  |    |    |--📄user.py 員工管理視圖
  |    |--📄models.py  定義了整個前後台網站的models
  |    |--📄shopmiddleware.py 定了整個網站的中間件（驗證是否登錄及權限管理）
  |    |--📄urls.py 配置了整個網站後台所有請求路由
  |
  |--📂web/ 前台應用（大堂點餐）
  |    |--📂views/
  |    |    |--📄cart.py 購物車管理視圖
  |    |    |--📄index.py 前臺的登錄、退出、驗證碼、加載店舖商品等方法
  |    |    |--📄orders.py 訂單管理視圖
  |    |--📄urls.py 配置了整個網站前台所有請求路由
  |
  |--📂myobject/ 項目目錄
  |    |--📄settings.py 設定前後臺app、中間件、TEMPLATES、STATICFILES
  |    |--📄urls.py 加載所有網站前後臺的路由
  |    |--📄wsgi.py
  |
  |--📂statics/ 靜態資源目錄
  |    |--📂uploads/   上傳文件、圖片的存儲目錄
  |    |--📂myadmin/   後臺管理靜態資源目錄
  |    |--📂web/       前臺管理靜態資源目錄
  |
  |--📂templates/ 模板目錄
  |    |--📂myadmin/   後台管理模板目錄
  |    |--📂web/       前台管理模板目錄
  |
  |--📄manage.py 入口文件
````
## 🗃  MYSQL設計數據表結構：

![111](https://user-images.githubusercontent.com/79140074/141604781-71f8c0f0-23fd-4caf-a3b7-65aa721659fe.png)
![222](https://user-images.githubusercontent.com/79140074/141604783-7bd788b8-d6a4-4839-aeaa-1f0f9bc7e13d.png)
![333](https://user-images.githubusercontent.com/79140074/141604671-07d432e1-b090-44b0-b6eb-019781501297.png)
![444](https://user-images.githubusercontent.com/79140074/141604787-8fa877e4-165b-4979-be9a-9d455c180b16.png)

## 👨‍💼  後臺員工系統網站介紹：

![00](https://user-images.githubusercontent.com/79140074/141610343-19a2d2da-c345-465a-99bb-e9c2c4d6c3b0.png)
後臺員工系統登入窗口
****
![1](https://user-images.githubusercontent.com/79140074/141613112-489ed84d-947b-451b-b3db-a69583d00b2b.png)

後臺首頁 ※備註：紅色框框為替換網頁內容區域，其餘為固定子視圖（base.html）； 以下後臺圖片只會顯示紅色框框的網頁內容
****
![2](https://user-images.githubusercontent.com/79140074/141612125-d64750b8-140d-4c81-b1b5-dfcfb381740f.png)
員工管理：瀏覽員工信息、添加員工及修改員工信息
****
![2](https://user-images.githubusercontent.com/79140074/141612786-046deb47-0e03-40f5-90e9-483eb3d3af9f.png)
店鋪管理：瀏覽各店鋪信息、添加店鋪及修改店鋪信息
****
![4](https://user-images.githubusercontent.com/79140074/141612687-7266d75d-bdf3-4d1b-ab33-52ceefedc378.png)
菜品類別管理：瀏覽各店鋪菜品分類信息、添加菜品分類及修改菜品分類信息，查看菜品則會跳到該分類的菜品信息
****
![5](https://user-images.githubusercontent.com/79140074/141612872-46327e26-2b61-4c64-8fd8-81245fab799c.png)
菜品信息管理：瀏覽各店鋪菜品信息、添加菜品信息及修改菜品信息
****
![6](https://user-images.githubusercontent.com/79140074/141612965-1906a8fd-cd16-4ef2-9fd7-8b95b8540a36.png)
會員管理：瀏覽各會員信息

## 👨‍🍳  前臺食堂系統網站介紹：

![11](https://user-images.githubusercontent.com/79140074/141613527-c326a3b9-ed47-4ac7-ae8b-24a74042532b.png)
前臺食堂系統登入窗口
****
![12](https://user-images.githubusercontent.com/79140074/141614066-b65ddf00-90e2-4727-9f94-bd57c2ca351f.png)
食堂點餐首頁：瀏覽選擇的該店鋪菜品信息、點選購物則會在購物車中顯示購物清單，按結算則資料會入當前訂單內，並做清空
****
