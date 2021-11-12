from django.db import models
from datetime import datetime

#員工帳號信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    #員工帳號
    nickname = models.CharField(max_length=50)    #暱稱
    password_hash = models.CharField(max_length=100)#密碼
    password_salt = models.CharField(max_length=50)    #密碼干擾值
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "user"  # 更改表名


#店鋪信息模型
class Shop(models.Model):
    name = models.CharField(max_length=255)        #店铺名稱
    cover_pic = models.CharField(max_length=255) #封面圖片
    banner_pic = models.CharField(max_length=255)#圖標Logo
    address = models.CharField(max_length=255)    #店鋪地址
    phone = models.CharField(max_length=255)    #聯絡電話
    status = models.IntegerField(default=1)        #狀態:1正常/2暂停/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        shopname = self.name.split("-")
        return {'id':self.id,'name':shopname[0],'shop':shopname[1],'cover_pic':self.cover_pic,'banner_pic':self.banner_pic,'address':self.address,'phone':self.phone,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "shop"  # 更改表名


#菜品分類信息模型
class Category(models.Model):
    shop_id = models.IntegerField()        #店鋪id
    name = models.CharField(max_length=50)  #分類名稱
    status = models.IntegerField(default=1)        #狀態:1正常/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    class Meta:
        db_table = "category"  # 更改表名


#菜品信息模型
class Product(models.Model):
    shop_id = models.IntegerField()        #店铺id
    category_id = models.IntegerField()    #菜品分类id
    cover_pic = models.CharField(max_length=50)    #菜品圖片
    name = models.CharField(max_length=50)  #菜品名稱
    price = models.FloatField()    #菜品單價
    status = models.IntegerField(default=1)        #狀態:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'shop_id':self.shop_id,'category_id':self.category_id,'cover_pic':self.cover_pic,'name':self.name,'price':self.price,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "product"  # 更改表名


#会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)    #暱稱
    avatar = models.CharField(max_length=255)    #頭像
    mobile = models.CharField(max_length=50)    #電話
    status = models.IntegerField(default=1)        #狀態:1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'nickname':self.nickname,'avatar':self.avatar,'mobile':self.mobile,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "member"  # 更改表名


# 订单模型
class Orders(models.Model):
    shop_id = models.IntegerField()   #店鋪id號
    member_id = models.IntegerField() #會員id
    user_id = models.IntegerField()   #操作員id
    money = models.FloatField()     #金額
    status = models.IntegerField(default=1)   #訂單狀態:1進行中/2無效/3已完成
    payment_status = models.IntegerField(default=1)   #支付狀態:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #創建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "orders"  # 更改表名


#定單詳情模型
class OrderDetail(models.Model):
    order_id = models.IntegerField()  #訂單id
    product_id = models.IntegerField()  #菜品id
    product_name = models.CharField(max_length=50) #菜品名稱
    price = models.FloatField()     #單價
    quantity = models.IntegerField()  #數量
    status = models.IntegerField(default=1) #狀態:1正常/9删除

    class Meta:
        db_table = "order_detail"  # 更改表名


# 支付信息模型
class Payment(models.Model):
    order_id = models.IntegerField()  #訂單id號
    member_id = models.IntegerField() #會員id
    money = models.FloatField()     #支付金額
    type = models.IntegerField()      #付款方式：1會員付款/2收銀收款
    bank = models.IntegerField(default=1) #收款银行渠道:1信用卡/2餘额/3現金/4手機支付
    status = models.IntegerField(default=1) #支付狀態:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #創建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "payment"  # 更改表名