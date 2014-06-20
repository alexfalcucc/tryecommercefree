from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import Contact
from .forms import ContactForm

def contact_us(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()
	return render(request, 'contact/contact_us.html', {'form':form})