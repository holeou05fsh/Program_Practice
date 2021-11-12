#後臺管理子路由文件
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import shop
from myadmin.views import category
from myadmin.views import product
from myadmin.views import member

urlpatterns = [
    #後臺首頁
    path('', index.index, name='myadmin_index'),

    #後臺管理員登入、退出
    path('login', index.login, name='myadmin_login'),
    path('dologin', index.dologin, name='myadmin_dologin'),
    path('logout', index.logout, name='myadmin_logout'),
    path('verify', index.verify, name='myadmin_verify'),

    #員工信息管理verify
    path('user/<int:pIndex>', user.index, name='myadmin_user_index'), #瀏覽
    path('user/add', user.add, name='myadmin_user_add'), #新增
    path('user/insert', user.insert, name='myadmin_user_insert'),  #執行新增
    path('user/del/<int:uid>', user.delete, name='myadmin_user_del'),  #刪除
    path('user/edit/<int:uid>', user.edit, name='myadmin_user_edit'),  #修改
    path('user/update/<int:uid>', user.update, name='myadmin_user_update'),  #執行修改

    # 店鋪信息管理
    path('shop/<int:pIndex>', shop.index, name='myadmin_shop_index'),  # 瀏覽
    path('shop/add', shop.add, name='myadmin_shop_add'),  # 新增
    path('shop/insert', shop.insert, name='myadmin_shop_insert'),  # 執行新增
    path('shop/del/<int:sid>', shop.delete, name='myadmin_shop_del'),  # 刪除
    path('shop/edit/<int:sid>', shop.edit, name='myadmin_shop_edit'),  # 修改
    path('shop/update/<int:sid>', shop.update, name='myadmin_shop_update'),  # 執行修改

    # 菜品類別信息管理
    path('category/<int:pIndex>', category.index, name='myadmin_category_index'),  # 瀏覽
    path('category/add', category.add, name='myadmin_category_add'),  # 新增
    path('category/insert', category.insert, name='myadmin_category_insert'),  # 執行新增
    path('category/del/<int:cid>', category.delete, name='myadmin_category_del'),  # 刪除
    path('category/edit/<int:cid>', category.edit, name='myadmin_category_edit'),  # 修改
    path('category/update/<int:cid>', category.update, name='myadmin_category_update'),  # 執行修改
    path('category/load/<int:sid>', category.loadCategory, name='myadmin_category_load'),  # 執行修改

    # 菜品信息管理
    path('product/<int:pIndex>', product.index, name='myadmin_product_index'),  # 瀏覽
    path('product/add', product.add, name='myadmin_product_add'),  # 新增
    path('product/insert', product.insert, name='myadmin_product_insert'),  # 執行新增
    path('product/del/<int:pid>', product.delete, name='myadmin_product_del'),  # 刪除
    path('product/edit/<int:pid>', product.edit, name='myadmin_product_edit'),  # 修改
    path('product/update/<int:pid>', product.update, name='myadmin_product_update'),  # 執行修改

    # 會員信息管理
    path('member/<int:pIndex>', member.index, name='myadmin_member_index'),  # 瀏覽
]
