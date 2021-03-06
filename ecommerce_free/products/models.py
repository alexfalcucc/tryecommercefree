from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=220)
	description = models.CharField(max_length=3000, null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	slug = models.SlugField(_('Slug'))
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self): return self.title
	
	class Meta:
		ordering = ['title',]
			
#very cool import for save images.
#from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location='/media/product/')

class ProductImage(models.Model):
	product = models.ForeignKey('Product')
	description = models.CharField(max_length=3000, null=True, blank=True)
	image = models.ImageField(upload_to='product/images/')
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self): return str(self.image)