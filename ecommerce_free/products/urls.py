# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('ecommerce_free.products.views',
    url(r'^$', 'all_products', name='products'),
    url(r'^(?P<slug>.*)/$', 'single_product'),
)