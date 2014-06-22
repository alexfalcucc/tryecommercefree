# coding: utf-8
from django.contrib import admin
from .models import Address, Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	class Meta: model = Profile

class AddressAdmin(admin.ModelAdmin):
	class Meta: model = Address


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address, AddressAdmin)