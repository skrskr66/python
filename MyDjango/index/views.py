from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required


#使用login_required和permission_required分别对用户登陆和用户权限进行验证
@login_required(login_url='/user/login.html')
@permission_required(perm='index.visit_Product',login_url='/user/login.html')
def index(request):
    #获取GET请求参数
    product = request.GET.get('product','')
    price = request.GET.get('price', '')
    if product:
        #获取存储在Session中的数据，若Session不存在product_info,则返回一个空列表
        product_list = request.session.get('product_info', [])
        #判断当前请求参数是否已存储在Session
        if not product in product_list:
            #将当前参数存储在列表product_list中
            product_list.append({'price':price,'product':product})
        #更新存储在Session中的数据
        request.session['product_info'] = product_list
        return redirect('/')
    return render(request, 'index.html', locals())

#视图函数ShoppingCarView
@login_required(login_url='/user/login.html')
def ShoppingCarView(request):
    #获取存储在Session中的数据，若Session中不存在product_info,则返回一个空列表
    product_list = request.session.get('product_info', [])
    #获取GET请求参数，若没有请求参数，则返回空值
    del_product = request.GET.get('product', '')
    #判断是否为空，若非空，则删除Session中的商品信息
    if del_product:
        #删除Session中某个商品
        for i in product_list:
            if i['product'] == del_product:
                product_list.remove(i)
            #将删除后的数据覆盖原来的Session
        request.session['product_info'] = product_list
        return redirect('/ShoppingCar.html')
    return render(request, 'ShoppingCar.html', locals())

