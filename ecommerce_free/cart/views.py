from django.shortcuts import (render, HttpResponse, HttpResponseRedirect, 
                                Http404, render_to_response, RequestContext, get_object_or_404)

from django.contrib import messages
# Create your views here.

from ecommerce_free.products.models import Product
from .models import Cart, CartItem
from .forms import ProductQtyForm

def add_to_cart(request):
    request.session.set_expiry(30)#seconds
    try: 
        cart_id = request.session['cart_id']
    except Exception:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id
        cart_id = cart.id
    if request.method == 'POST':
        form_cart = ProductQtyForm(request.POST)
        if form_cart.is_valid():
            product_slug = form_cart.cleaned_data['slug']
            product_quantity = form_cart.cleaned_data['quantity']
            try:
                product = Product.objects.get(slug=product_slug)
            except Exception:
                product = None
            try:
                cart = Cart.objects.get(id=cart_id)
            except Exception:
                cart = None

            new_cart, created = CartItem.objects.get_or_create(cart=cart, product=product)
            new_cart.quantity = product_quantity
            new_cart.save()
            if created:
                print 'Criado!'
            
            
            return HttpResponseRedirect('/cart/')
        return HttpResponseRedirect('/contact/')
    else:
        raise Http404

def view(request):
    request.session.set_expiry(30)
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
    except Exception:
        cart = Cart()

    cart_items = len(CartItem.objects.all())

    if not cart_items:
        messages.add_message(request, messages.ERROR, 'Seu carrinho esta vazio! =/')
        if cart == False or cart.active == False:
            messages.add_message(request, messages.ERROR, 'Seu carrinho esta vazio! =/')
        else:
            pass

    if cart and cart.active: cart = cart

    request.session['cart_items'] = len(CartItem.objects.all())

    context = {'cart':cart, 'items':CartItem.objects.all()}

    return render(request, 'cart/view_cart.html', context)
    

    
