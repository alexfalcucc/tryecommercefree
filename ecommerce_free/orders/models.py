# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from ecommerce_free.cart.models import Cart 
from .custom import id_generator
# Create your models here.

STATUS_CHOICES = (
		('Started','Started'),
		('Abandoned','Abandoned'),
		('Collected','Collected'),
)

class Order(models.Model):
	user = models.ForeignKey(User)
	cart = models.ForeignKey(Cart)
	order_id = models.CharField(max_length=120, default="ABC123")
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
		
	def __unicode__(self, ):
		return "Order number is %s" %(self.order_id)

	def save(self, ):
		new_number = id_generator()
		self.order_id = str(new_number[:2]) + str(self.cart.id) + str(new_number[3:])
		super(Order, self).save()
		