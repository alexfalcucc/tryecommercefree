from django.shortcuts import (render, HttpResponse, HttpResponseRedirect, 
                                Http404, render_to_response, RequestContext, get_object_or_404)
import datetime
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

from ecommerce_free.products.models import Product
from .models import Cart, CartItem
from .forms import ProductQtyForm
from ecommerce_free.profiles.models import Profile

from django.db.models import Count

import stripe
stripe.api_key = "sk_test_g75PwGm4d1FQR5odRu4xKwka"

@login_required
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
            if product_quantity > 0:
                new_cart.quantity = product_quantity
                new_cart.total = int(new_cart.quantity) * new_cart.product.price
                new_cart.save()
            else:
                pass
            if created:
                print 'Criado!'
            
            
            return HttpResponseRedirect('/cart/')
        return HttpResponseRedirect('/contact/')
    else:
        raise Http404

def add_stripe(user):
    profile, created = Profile.objectts.get_or_create(user=user)
    if len(profile.stripe_id) > 1: 
        print 'Existente!'
    else: 
        new_customer = stripe.Customer.Create(
                email = user.email,
                description = 'Stripe adicionado em %s' %(datetime.datetime.now())
        )
        profile.stripe_id = new_customer.id
        profile.save()
    return profile.stripe_id



@login_required
def view(request):
    request.session.set_expiry(300)
    #cart_items = len(CartItem.objects.all())
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        cart_items = len(CartItem.objects.all())
    except Exception:
        cart = Cart()
    #if not cart_items:
    #   messages.add_message(request, messages.ERROR, 'Seu carrinho esta vazio! =/')
    if cart == False or cart.active == False:
        messages.add_message(request, messages.ERROR, 'Seu carrinho esta vazio! =/')
    else:
        pass
    
    cart.total = 0
    for item in CartItem.objects.all(): 
        cart.total += int(item.total)
        cart.save()

    if cart and cart.active: cart = cart

    try:
        stripe_id = add_stripe(request.user)
    except Exception:
        pass

    
    context = {'cart':cart, 'items':CartItem.objects.all(), 'cart_items':cart_items,}

    return render(request, 'cart/view_cart.html', context)
    
@login_required
def checkout(request):
    print request.POST
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
    except Exception:
        cart = Cart()

    amount = int(cart.total * 100)
    
    try:
        stripe_id = add_stripe(request.user)
    except Exception:
        pass

    if request.method == 'POST':
        token = u'tok_104GZg4fG5cN4uqf2EPpccn7'
        profile = request.user.get_profile()
        stripe.Charge.create(
                amount=amount,
                currency="usd",
                card=token,
                description=None
        )

    cart_items = len(CartItem.objects.all())
    
    return render(request, 'cart/checkout.html', {'cart_items':cart_items})