from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=300, null=True, blank=True)
	email = models.EmailField()
	message = models.TextField(max_length=500, verbose_name='Mensagem')
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self): return "Mensagem para " + str(self.email)


