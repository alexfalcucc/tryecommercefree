from django.db import models
from django.contrib.auth.models import User

from ecommerce_free.products.models import Product

# Create your models here.

class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.id)

class CartItem(models.Model):
	cart = models.ForeignKey('Cart')
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.cart.id)
