from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ecommerce_free.cart.forms  import ProductQtyForm
from ecommerce_free.cart.models import CartItem

from .models import Product

# Create your views here.

def all_products(request):
	request.session['cart_items'] = len(CartItem.objects.all())
	products = Product.objects.filter(active=True)
	context = {'products':products,}
	return render(request, 'products/all_products.html', context)

def single_product(request, slug):
	add_product = ProductQtyForm()
	product = get_object_or_404(Product, slug=slug)
	return render(request, 'products/single_product.html', {'product':product, 'add_product':add_product})