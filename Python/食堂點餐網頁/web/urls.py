#前臺餐廳點餐子路由文件
from django.urls import path, include
from web.views import index, cart, orders

urlpatterns = [
    path('', index.index, name='index'),

    #前台登陸
    path('login', index.login, name='web_login'),
    path('dologin', index.dologin, name='web_dologin'),
    path('logout', index.logout, name='web_logout'),
    path('verify', index.verify, name='web_verify'),

    #url路由添加，請求前綴
    path('web/', include([
        path('', index.webindex, name='web_index'), #前台大堂點餐首頁

        #購物車信息管理路由
        path('cart/add/<str:pid>', cart.add, name='web_cart_add'), #前台大堂點餐首頁
        path('cart/del/<str:pid>', cart.delete, name='web_cart_delete'),  # 前台大堂點餐首頁
        path('cart/clear', cart.clear, name='web_cart_clear'),  # 前台大堂點餐首頁
        path('cart/change', cart.change, name='web_cart_change'),  # 前台大堂點餐首頁

        #訂單處理路由
        path('orders/insert', orders.insert, name='web_orders_insert'),  #執行訂單添加
        path('orders/<int:pIndex>', orders.index, name='web_orders_index'),  #執行訂單瀏覽
        path('orders/detail', orders.detail, name='web_orders_detail'),  #執行訂單詳情
        path('orders/status', orders.status, name='web_orders_status'),  #執行訂單狀態
    ]))
]