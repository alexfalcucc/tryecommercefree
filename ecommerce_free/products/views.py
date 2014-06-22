from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from ecommerce_free.cart.forms  import ProductQtyForm
from ecommerce_free.cart.models import CartItem

from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.


def all_products(request):
	cart_items = len(CartItem.objects.all())
	products = Product.objects.filter(active=True)
	context = {'products':products, 'cart_items':cart_items}
	return render(request, 'products/all_products.html', context)

@login_required
def single_product(request, slug):
	cart_items = len(CartItem.objects.all())
	add_product = ProductQtyForm()
	product = get_object_or_404(Product, slug=slug)
	context = {
		'product':product, 'add_product':add_product, 'cart_items':cart_items,
	}
	return render(request, 'products/single_product.html', context)