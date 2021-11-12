from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Shop
from django.core.paginator import Paginator
import time
from datetime import datetime

# Create your views here.
#瀏覽
def index(request, pIndex=1):
    smod = Shop.objects
    slist = smod.filter(status__lt = 9)
    mywhere = []
    #獲取並判斷搜尋條件
    kw = request.GET.get('keyword', None)
    if kw:
        slist = slist.filter(name__contains=kw)
        mywhere.append('keyword='+kw)
    status = request.GET.get('status', '')
    if status != '':
        slist = slist.filter(status=status)
        mywhere.append('status'+status)

    slist = slist.order_by('id')  #要做排序，不然第一次查詢會不能運行(影片25集5:20)
    #分頁處理
    pIndex = int(pIndex)
    page = Paginator(slist, 5) #以每頁5條數據分頁
    maxpages = page.num_pages #獲得最大頁數
    #判斷當前頁數
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1 :
        pIndex = 1
    list2 = page.page(pIndex) #獲取當前數據
    plist = page.page_range
    context = {"shoplist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'myadmin/shop/index.html', context)
#新增
def add(request):
    return render(request, 'myadmin/shop/add.html')
#執行新增
def insert(request):
    try:
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse('沒有封面上傳')
        cover_pic = str(time.time()).split(".").pop()+'.'+myfile.name.split(".").pop()
        destination = open('./statics/uploads/shop/'+cover_pic, 'wb+')
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()

        myfile = request.FILES.get("banner_pic", None)
        if not myfile:
            return HttpResponse('沒有logo上傳')
        banner_pic = str(time.time()).split(".").pop()+'.'+myfile.name.split(".").pop()
        destination = open('./statics/uploads/shop/'+banner_pic, 'wb+')
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()

        ob = Shop()
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.cover_pic = cover_pic
        ob.banner_pic = banner_pic
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
def delete(request, sid=0):
    try:
        ob = Shop.objects.get(id=sid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '刪除成功'}
    except Exception as err:
        print(err)
        context = {'info': '刪除失敗'}
    return render(request, "myadmin/info.html", context)
#修改
def edit(request, sid=0):
    try:
        ob = Shop.objects.get(id=sid)
        context = {'shop': ob}
        return render(request, "myadmin/Shop/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '無此信息'}
        return render(request, "myadmin/info.html", context)
#執行修改
def update(request, sid):
    try:
        ob = Shop.objects.get(id=sid)
        ob.name = request.POST['name']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':"修改成功"}
    except Exception as err:
        print(err)
        context = {'info':'修改失敗'}
    return render(request, 'myadmin/info.html', context)

