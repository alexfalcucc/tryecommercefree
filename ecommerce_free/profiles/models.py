# coding: utf-8
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	stripe_id = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.user)


class Address(models.Model):
	user = models.ForeignKey(User)
	nickname = models.CharField(max_length=120, null=True, blank=True)
	address1 = models.CharField(max_length=300)
	address2 = models.CharField(max_length=300, null=True, blank=True)
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	country = models.CharField(max_length=300)
	cep = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	default_address = models.BooleanField(default=False)
	billing_address = models.CharField(max_length=300, default=False)#cash in
	shipping_address = models.CharField(max_length=300, default=False)#endereco de envio.

	def __unicode__(self):
		return self.address1
