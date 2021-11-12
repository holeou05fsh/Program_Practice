from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator
from datetime import datetime
from myadmin.models import User, Orders, OrderDetail, Payment

# Create your views here.
def insert(request):
    '''訂單添加'''
    try:
        #執行訂單信息添加
        ob = Orders()
        ob.shop_id = request.session['shopinfo']['id']
        ob.member_id = 0
        ob.user_id = request.session['webuser']['id']
        ob.money = request.session['total_money']
        ob.status = 1  #訂單狀態:1过行中/2無效/3已完成
        ob.payment_status = 2  #支付狀態:1未支付/2已支付/3已退款
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()

        #執行支付信息添加
        op = Payment()
        op.order_id = ob.id  # 訂單id號
        op.member_id = 0  # 會員id
        op.money = request.session['total_money']  # 支付金額
        op.type = 2  # 付款方式：1會員付款/2收銀收款
        op.bank = request.GET.get('bank', 3)  #收款银行渠道:1信用卡/2餘额/3現金/4手機支付
        op.status = 1  # 支付狀態:1未支付/2已支付/3已退款
        op.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        op.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        op.save()

        #執行訂單詳情添加
        cartlist = request.session.get('cartlist', {})
        #迴圈購物車中的菜品信息

        for i in cartlist.values():
            od = OrderDetail()
            od.order_id = ob.id  #訂單id
            od.product_id = i['id']  #菜品id
            od.product_name = i['name']  #菜品名稱
            od.price = i['price']  #單價
            od.quantity = i['num']  #數量
            od.status = 1  #狀態:1正常/9删除
            od.save()

        del request.session['cartlist']
        del request.session['total_money']
        return HttpResponse('Y')
    except Exception as err:
        print(err)
    return HttpResponse('N')

def index(request, pIndex=1):
    '''瀏覽訂單'''
    umod = Orders.objects.all()
    # 獲取當前店鋪ID號
    sid = request.session['shopinfo']['id']
    ulist = umod.filter(shop_id = sid)
    # ulist.
    # bank = Payment.objects.only('bank')
    # bank.append(ulist)
    # print(bank)
    mywhere = []
    #獲取、判斷並封裝狀態status搜尋條件
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append('?status='+status)

    ulist = ulist.order_by('id')  #要做排序，不然第一次查詢會不能運行(25,5:20)
    #分頁處理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10)  #以每頁10條數據分頁
    maxpages = page.num_pages  #獲得最大頁數
    #判斷當前頁數
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #獲取當前數據
    plist = page.page_range
    for i in list2:
        if i.user_id == 0:
            i.nickname = '無'
        else:
            user = User.objects.only('nickname').get(id=i.user_id)
            i.nickname = user.nickname

    context = {"orderslist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'web/list.html', context)

def detail(request):
    '''查看訂單內容'''
    oid = request.GET.get('oid', 0)  #oid是js的functiondo內doshow中的oid值
    dlist = OrderDetail.objects.filter(order_id=oid)
    context = {'detaillist':dlist}
    return render(request, 'web/datail.html', context)

def status(request):
    '''修改訂單狀態'''
    try:
        oid = request.GET.get('oid', 0)
        ob = Orders.objects.get(id=oid)
        ob.status = request.GET['status']
        ob.save()
        return HttpResponse('Y')
    except Exception as err:
        print(err)
        return HttpResponse('N')
