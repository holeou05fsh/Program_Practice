from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import User
#後台管理員首頁
def index(request):
    return render(request, 'myadmin/index/index.html')

#管理員登入表單
def login(request):
    return render(request, 'myadmin/index/login.html')

#執行管理員登入
def dologin(request):
    try:
        #驗證碼驗證
        if request.POST['code'] != request.session['verifycode']:
            context = {"info": "驗證碼錯誤"}
            return render(request, 'myadmin/index/login.html', context)
        #根據登錄帳號獲得登入者信息
        user = User.objects.get(username=request.POST['username'])
        #判斷當前用戶是否是管理員
        if user.status == 6:
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pass'] + str(user.password_salt)  # 表中的密碼+隨機數干擾值
            md5.update(s.encode('utf-8'))  # 將要產生md5的字串放入
            if user.password_hash == md5.hexdigest():  # 獲取md5
                print('登入成功')
                #將當前登錄成功用戶信行已adminuser為key寫入session中
                request.session['adminuser'] = user.toDict()
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info':'登錄密碼錯誤'}
        else:
            context = {'info':'無效的登錄帳號'}
    except Exception as err:
        print(err)
        context = {"info":"帳號不存在"}
    return render(request, 'myadmin/index/login.html', context)

#管理員登出
def logout(request):
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))
#驗證碼
def verify(request):
    #引入隨機函數模塊
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定義變量，用於畫面的背景色、寬、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #創建畫面對象
    im = Image.new('RGB', (width, height), bgcolor)
    #創建畫筆對象
    draw = ImageDraw.Draw(im)
    #調用畫筆的point()函數繪製噪點
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定義驗證碼的備選值
    #str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    #隨機選取4個值作為驗證碼
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #構造字體對象，ubuntu的字體路徑為“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 21)
    #font = ImageFont.load_default().font
    #構造字體顏色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #繪製4個字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    #釋放畫筆
    del draw
    #存入session，用於做進一步驗證
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 內存文件操作-->此方法為python3的
    import io
    buf = io.BytesIO()
    #將圖片保存在內存中，文件類型為png
    im.save(buf, 'png')
    #將內存中的圖片數據返回給客戶端，MIME類型為圖片png
    return HttpResponse(buf.getvalue(), 'image/png')
