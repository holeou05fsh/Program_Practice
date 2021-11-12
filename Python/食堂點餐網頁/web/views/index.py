from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from myadmin.models import User, Shop, Category, Product

# Create your views here.
def index(request):
    return redirect(reverse('web_index'))

def webindex(request):
    # 從session中取出cartlist的購物車訊息，如果沒有就給他一個{}dict
    cartlist = request.session.get('cartlist', {})
    total_money = 0 #初始劃一個總金額
    #購物車中的菜品累加總金額
    for i in cartlist.values():
        total_money += i['price'] * i['num']
    request.session['total_money'] = total_money
    #將session中的菜品和類別信息獲取並items轉換(轉換可讓pids每個菜品信息排序), 才可實現for迴圈的放入
    context = {'categorylist': request.session.get('categorylist', {}).items()}
    # print(request.session.get('categorylist'))
    # print(context)
    return render(request, 'web/index.html', context)

def login(request):
    shoplist = Shop.objects.filter(status=1)
    context = {'shoplist':shoplist}
    return render(request, 'web/login.html', context)

def dologin(request):
    try:
        #是否選擇店鋪
        if request.POST['shop_id'] == '0':
            return redirect(reverse('web_login') + '?errinfo=1')
        #驗證碼驗證
        if request.POST['code'] != request.session['verifycode']:
            return redirect(reverse('web_login') + '?errinfo=2')
        #根據登錄帳號獲得登入者信息
        user = User.objects.get(username=request.POST['username'])
        #判斷當前用戶否是是管理員或正常
        if user.status == 6 or user.status == 1:
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pass'] + str(user.password_salt)  # 表中的密碼+隨機數干擾值
            md5.update(s.encode('utf-8'))  # 將要產生md5的字串放入
            if user.password_hash == md5.hexdigest():  # 獲取md5
                print('登入成功')
                #將當前登錄成功用戶信行已adminuser為key寫入session中
                request.session['webuser'] = user.toDict()
                #獲取當前店鋪信息
                shopob = Shop.objects.get(id=request.POST['shop_id'])
                # print(shopob)
                request.session['shopinfo'] = shopob.toDict()
                #獲取當前店鋪所有的派品類別和菜品信息
                clist = Category.objects.filter(shop_id=shopob.id, status=1)
                categorylist = dict() #菜品類別(內有菜品信息)
                productlist = dict() #菜品信息
                #放入菜品類別
                for i in clist:
                    c = {'id':i.id, 'name':i.name, 'pids':[]}
                    plist = Product.objects.filter(category_id=i.id, status=1)
                    #在菜品類別(pid)中放入菜品信息
                    for p in plist:
                        c['pids'].append(p.toDict())
                        productlist[p.id] = p.toDict()
                    categorylist[i.id] = c
                    #將上面的結果存入到session中
                    request.session['categorylist'] = categorylist
                    request.session['productlist'] = productlist
                # print(productlist)
                return redirect(reverse('web_index'))
            else:
                return redirect(reverse('web_login') + '?errinfo=5')
        else:
            return redirect(reverse('web_login') + '?errinfo=4')
    except Exception as err:
        print(err)
        return redirect(reverse('web_login') + '?errinfo=3')

def logout(request):
    del request.session['webuser']
    return redirect(reverse('web_login'))

def verify(request):
    # 引入随機函數模塊
    import random
    from PIL import Image, ImageDraw, ImageFont  #随機義變繪創對畫筆義驗證碼的備選體對構
    # 定義變量，用于畫面的背景色、寬、高
    # bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242, 164, 247)
    width = 130
    height = 40
    # 創建畫面對象
    im = Image.new('RGB', (width, height), bgcolor)
    # 創建畫筆對象
    draw = ImageDraw.Draw(im)
    # 調用畫筆的point()函數繪制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定義驗證碼的備選值
    # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    # 随機選取4个值作為驗證碼
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 構造字體對象，ubuntu的字體路徑為“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 36)
    # font = ImageFont.load_default().font
    # 構造字體颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 繪制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((35, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((70, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((100, -3), rand_str[3], font=font, fill=fontcolor)
    # 釋放畫筆
    del draw
    # 存入session，用于做進一步驗證
    request.session['verifycode'] = rand_str
    """
    python2的為
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法為python3的
    import io
    buf = io.BytesIO()
    # 將圖片保存在内存中，文件類型為png
    im.save(buf, 'png')
    # 將内存中的圖片數據返回给客户端，MIME類型為圖片png
    return HttpResponse(buf.getvalue(), 'image/png')