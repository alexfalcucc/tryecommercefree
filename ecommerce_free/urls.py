# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ecommerce_free.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('ecommerce_free.products.urls')),
    url(r'^cart/', include('ecommerce_free.cart.urls')),
    url(r'^contact/', 'ecommerce_free.contact.views.contact_us', name='contact_us'),
    url(r'^checkout/', 'ecommerce_free.cart.views.checkout', name='checkout'),



) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
