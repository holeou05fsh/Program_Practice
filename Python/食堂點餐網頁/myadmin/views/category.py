from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Category, Shop
from django.core.paginator import Paginator
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
#瀏覽
def index(request, pIndex=1):
    cmod = Category.objects
    clist = cmod.filter(status__lt = 9)
    mywhere = []
    #獲取並判斷搜尋條件
    kw = request.GET.get('keyword', None)
    if kw:
        clist = clist.filter(name__contains=kw)
        mywhere.append('keyword='+kw)
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
    #遍歷當前菜品分類管理，並封裝對應的片鋪信息
    for v in list2:
        sob = Shop.objects.get(id=v.shop_id)
        v.shopname = sob.name

    context = {"categorylist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'myadmin/category/index.html', context)
#javascript的選單
def loadCategory(request, sid):
    clist = Category.objects.filter(status__lt=9, shop_id=sid).values('id', 'name')
    return JsonResponse({'data':list(clist)})
#新增
def add(request):
    slist = Shop.objects.values('id', 'name')
    context = {'shoplist':slist}
    return render(request, 'myadmin/category/add.html', context)
#執行新增
def insert(request):
    try:
        ob = Category()
        ob.shop_id = request.POST['shop_id']
        ob.name = request.POST['name']
        ob.status = 1
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':'新增成功'}
    except Exception as err:
        context = {'info':'新增失敗'}
    return render(request, "myadmin/info.html", context)

#刪除
def delete(request, cid=0):
    try:
        ob = Category.objects.get(id=cid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '刪除成功'}
    except Exception as err:
        print(err)
        context = {'info': '刪除失敗'}
    return render(request, "myadmin/info.html", context)
#修改
def edit(request, cid=0):
    try:
        slist = Shop.objects.values('id', 'name')
        context = {'shoplist': slist}
        ob = Category.objects.get(id=cid)
        context['category'] = ob
        return render(request, "myadmin/category/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '無此信息'}
        return render(request, "myadmin/info.html", context)
#執行修改
def update(request, cid):
    try:
        ob = Category.objects.get(id=cid)
        ob.shop_id = request.POST['shop_id']
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':"修改成功"}
    except Exception as err:
        print(err)
        context = {'info':'修改失敗'}
    return render(request, 'myadmin/info.html', context)

