from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Member
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.
#瀏覽
def index(request, pIndex=1):
    umod = Member.objects
    ulist = umod.filter(status__lt = 9)
    mywhere = []
    #獲取並判斷搜尋條件
    kw = request.GET.get('keyword', None)
    if kw:
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append('keyword='+kw)
    status = request.GET.get('status', '')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append('status'+status)

    ulist = ulist.order_by('id')  #要做排序，不然第一次查詢會不能運行(影片25集5:20)
    #分頁處理
    pIndex = int(pIndex)
    page = Paginator(ulist, 5) #以每頁5條數據分頁
    maxpages = page.num_pages #獲得最大頁數
    #判斷當前頁數
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1 :
        pIndex = 1
    list2 = page.page(pIndex) #獲取當前數據
    plist = page.page_range
    context = {"memberlist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'myadmin/member/index.html', context)
#刪除
def delete(request, uid=0):
    try:
        ob = Member.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '刪除成功'}
    except Exception as err:
        print(err)
        context = {'info': '刪除失敗'}
    return render(request, "myadmin/info.html", context)
