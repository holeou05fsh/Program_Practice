from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Product, Category, Shop
from django.core.paginator import Paginator
from datetime import datetime
import time, os
# Create your views here.
#瀏覽
def index(request, pIndex=1):
    cmod = Product.objects
    clist = cmod.filter(status__lt = 9)
    mywhere = []
    #獲取並判斷搜尋條件
    kw = request.GET.get('keyword', None)
    if kw:
        clist = clist.filter(name__contains=kw)
        mywhere.append('?keyword='+kw)
    #獲取並判斷搜尋菜品類別條件
    cid = request.GET.get('category_id', None)
    if cid:
        clist = clist.filter(category_id=cid)
        mywhere.append('?category_id='+cid)
    status = request.GET.get('status', '')
    if status != '':
        clist = clist.filter(status=status)
        mywhere.append('status'+status)

    clist = clist.order_by('id')  #要做排序，不然第一次查詢會不能運行(影片25集5:20)
    #分頁處理
    pIndex = int(pIndex)
    page = Paginator(clist, 10) #以每頁10條數據分頁
    maxpages = page.num_pages #獲得最大頁數
    #判斷當前頁數
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #獲取當前數據
    plist = page.page_range
    #遍歷當前菜品信息管理，並封裝對應的片鋪及菜品類別信息
    for v in list2:
        sob = Shop.objects.get(id=v.shop_id)
        v.shopname = sob.name
        cob = Category.objects.get(id=v.category_id)
        v.categoryname = cob.name

    context = {"productlist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'myadmin/product/index.html', context)
#新增
def add(request):
    slist = Shop.objects.values('id', 'name')
    context = {'shoplist':slist}
    return render(request, 'myadmin/product/add.html', context)
#執行新增
def insert(request):
    try:
        #圖片上傳
        myfile = request.FILES.get('cover_pic')
        if not myfile:
            context = {'info': '沒有上傳圖片'}
            return render(request, "myadmin/info.html", context)
        cover_pic = str(time.time()).split('.').pop() +'.'+ myfile.name.split('.').pop()
        with open('./statics/uploads/product/'+cover_pic, 'wb+') as fp:
            for chunk in myfile.chunks():
                fp.write(chunk)

        ob = Product()
        ob.shop_id = request.POST['shop_id']
        ob.category_id = request.POST['category_id']
        ob.cover_pic = cover_pic
        ob.name = request.POST['name']
        ob.price = request.POST['price']
        ob.status = 1
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':'新增成功'}
    except Exception as err:
        print(err)
        context = {'info':'新增失敗'}
    return render(request, "myadmin/info.html", context)

#刪除
def delete(request, pid=0):
    try:
        ob = Product.objects.get(id=pid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '刪除成功'}
    except Exception as err:
        print(err)
        context = {'info': '刪除失敗'}
    return render(request, "myadmin/info.html", context)
#修改
def edit(request, pid=0):
    try:
        ob = Product.objects.get(id=pid)
        context = {'product': ob}
        slist = Shop.objects.values('id', 'name')
        context['shoplist'] = slist
        return render(request, "myadmin/product/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '無此信息'}
        return render(request, "myadmin/info.html", context)
#執行修改
def update(request, pid):
    try:
        oldpicname = request.POST['oldpicname']
        #圖片上傳
        myfile = request.FILES.get('cover_pic')
        if not myfile:
            cover_pic = oldpicname
        else:
            cover_pic = str(time.time()).split('.').pop() +'.'+ myfile.name.split('.').pop()
            with open('./statics/uploads/product/'+cover_pic, 'wb+') as fp:
                for chunk in myfile.chunks():
                    fp.write(chunk)

        ob = Product.objects.get(id=pid)
        ob.shop_id = request.POST['shop_id']
        ob.category_id = request.POST['category_id']
        ob.price = request.POST['price']
        ob.name = request.POST['name']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':"修改成功"}
        #成功上傳後刪除舊照片
        if myfile:
            os.remove('./statics/uploads/product/'+oldpicname)

    except Exception as err:
        print(err)
        context = {'info':'修改失敗'}
        #成功時刪除舊照片
        if myfile:
            os.remove('./statics/uploads/product/'+cover_pic)
    return render(request, 'myadmin/info.html', context)

