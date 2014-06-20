# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('ecommerce_free.cart.views',
    url(r'^add/$', 'add_to_cart'),
    url(r'^view/$', 'view', name='view_cart'),
)