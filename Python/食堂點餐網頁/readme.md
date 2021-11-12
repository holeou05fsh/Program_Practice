# Django開發-食堂系統網站

## 📢　前言：

在之前服務業的工作中，有許多點餐、叫餐的工作要做，而此服務也在花費了許多時間，也會有許多的問題發生，例如叫錯餐、少餐、忙碌而延餐、記帳錯誤等問題，許多狀況發生，而想寫這個點餐的網站。
    
## 🛠　項目使用技術：

* 使用Django框架，版本：2.2.*的LTS版本。
* MySQL數據庫。
* 連結數據庫：mysqlclient 2.0.3。
* 圖像處理： Pillow 8.4.0。
* Web前端技術：HTML、CSS、JavaScript和Jquery等。
* 前端代碼引用：https://github.com/ColorlibHQ/AdminLTE 、 www.xuebiancheng.cn

## 🎨　E-R圖 / 項目功能模塊圖
<img src="https://user-images.githubusercontent.com/79140074/141459842-0e438da2-6ce2-49ba-b9b0-cf54216b12c3.png" width="420">   <img src="https://user-images.githubusercontent.com/79140074/141459845-ee948a55-e651-4f2b-8893-db9aae4a99f0.png" width="457">

## 📝　員工後臺管理應用
網站後台模板採用github上提供的一個後台管理界面，

網址：https://github.com/ColorlibHQ/AdminLTE 、 https://github.com/alecfan/mstp_17_akira （已過時）

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



## 📝　食堂前臺管理應用
網站前台模板採用網址：www.xuebiancheng.cn的課程
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
