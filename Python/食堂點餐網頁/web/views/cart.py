from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
def add(request, pid):
    '''添加購物車操作'''
    #從session中獲取當前店鋪中所有菜品信息，並從中取要放入cart中的菜品
    product = request.session['productlist'][pid]
    product['num'] = 1 #初始化當前菜品的購物量
    #從session中取出cartlist的購物車訊息，如果沒有就給他一個{}dict
    cartlist = request.session.get('cartlist', {})
    #判斷當前購物車中，是否存在要放入的菜品
    if pid in cartlist:
        cartlist[pid]['num'] += product['num'] #如果有就增加購買量
    else:
        cartlist[pid] = product #如果沒有就把整個菜品信息放入
    request.session['cartlist'] = cartlist #要將cartlist放入購物車
    # print(request.session['cartlist'])
    return redirect(reverse('web_index'))

def delete(request, pid):
    '''刪除購物車操作'''
    # 從session中取出cartlist的購物車訊息，如果沒有就給他一個{}dict
    cartlist = request.session.get('cartlist',{})
    del cartlist[pid]
    request.session['cartlist'] = cartlist  # 在將cartlist放回session中
    #在跳回首頁
    return redirect(reverse('web_index'))

def clear(request):
    '''清空購物車操作'''
    request.session['cartlist'] = {}
    return redirect(reverse('web_index'))

def change(request):
    '''更改購物車商品數量操作'''
    cartlist = request.session.get('cartlist',{})
    pid = request.GET.get('pid', 0)  # 獲取要修改的菜品id
    print(pid)
    m = int(request.GET.get('num', 1)) #要修改的數量
    if m < 1:
        m = 1

    cartlist[pid]['num'] = m #修改購物車的數量
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))