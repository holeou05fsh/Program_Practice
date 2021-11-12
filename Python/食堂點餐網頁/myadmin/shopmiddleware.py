from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('ShopMiddleware')

    def __call__(self, request):
        path = request.path
        print('url:', path)

        #判斷管理後台是否登入
        #定義後台不登錄也可直接訪問的url列表
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin', '/myadmin/verify']
        #判斷當前請求url地址是否已/myadmin開頭，並且不在urllist中，才做是否登錄
        if re.match(r'^/myadmin', path) and (path not in urllist):
            #判斷是否登錄(在於session中沒有adminuser)
            if 'adminuser' not in request.session:
                #重定向跳登錄頁
                return redirect(reverse('myadmin_login'))


        # 判斷管理前台是否登入
        if re.match(r'^/web', path):
            #判斷是否登錄(在於session中沒有webuser)
            if 'webuser' not in request.session:
                #重定向跳登錄頁
                return redirect(reverse('web_login'))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response