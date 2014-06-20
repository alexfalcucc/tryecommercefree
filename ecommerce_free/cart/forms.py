from django import forms

from .models import Cart, CartItem

from ecommerce_free.products.models import Product

class ProductQtyForm(forms.ModelForm):
	quantity = forms.IntegerField()
	class Meta:
		model = Product
		fields = ['slug']