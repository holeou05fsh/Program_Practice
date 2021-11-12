from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

# Create your views here.
#瀏覽
def index(request, pIndex=1):
    umod = User.objects
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
    # print('plist:',plist, '  pIndex:',pIndex, ' list2:', list2, 'mywhere:',mywhere)
    context = {"userlist":list2, "plist":plist, "pIndex":pIndex, "maxpages":maxpages, 'mywhere':mywhere}
    return render(request, 'myadmin/user/index.html', context)
#新增
def add(request):
    return render(request, 'myadmin/user/add.html')
#執行新增
def insert(request):
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        #post回來的密碼做md5處理
        import hashlib, random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n) #表中的密碼+隨機數干擾值
        md5.update(s.encode('utf-8')) #將要產生md5的字串放入
        ob.password_hash = md5.hexdigest() #獲取md5
        ob.password_salt = n

        ob.status = 1
        ob.create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':'新增成功'}
    except Exception as err:
        context = {'info':'新增失敗'}
    return render(request, "myadmin/info.html", context)

#刪除
def delete(request, uid=0):
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info': '刪除成功'}
    except Exception as err:
        print(err)
        context = {'info': '刪除失敗'}
    return render(request, "myadmin/info.html", context)
#修改
def edit(request, uid=0):
    try:
        ob = User.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/user/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '無此信息'}
        return render(request, "myadmin/info.html", context)
#執行修改
def update(request, uid):
    try:
        ob = User.objects.get(id=uid)
        # ob.nickname = request.POST['username']
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ob.save()
        context = {'info':"修改成功"}
    except Exception as err:
        print(err)
        context = {'info':'修改失敗'}
    return render(request, 'myadmin/info.html', context)

