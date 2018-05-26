# -*- coding:utf-8 -*-

from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'^home/$',views.home),
    url(r'^market/(\w+)/(\w+)/(\w+)/$',views.market),
    url(r'^cart/$',views.cart),
    url(r'^mine/$',views.mine),
    #获取商品信息
    url(r'product/(\w+)/$',views.product),
    url(r'^login/$', views.login),
    url(r'quit/$', views.quit),
    url(r'adress/$', views.adress),
    url(r'showAddress/$', views.showAddress),
    url(r'addAddress/$', views.addAddress),
    # url(r'^changecart/$', views.changecart),
    # 修改购物车  增加、减少
    url(r'^changecart/(\d+)/$', views.changecart),
    # 修改购物车  是否选中
    url(r'^changecart2/$', views.changecart2),
    # 下订单
    url(r'^qOrder/$', views.qOrder),

]
