from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
	class Meta: model = Order

	def get_readonly_field(self, request, obj=None):
		if obj:
			return ['order_id']
		return self.readonly_fiels

admin.site.register(Order, OrderAdmin)