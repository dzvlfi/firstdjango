from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import random

# Create your views here.
class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args,**kwargs)
		num = None
		some_list = [
			random.randint(0, 1000),
			random.randint(0, 1000),
			random.randint(0, 1000)
		]
		condition_bool_item = True
		if condition_bool_item:
			num = random.randint(0, 1000)
		context = {
			"num": num,
			"some_list": some_list,
			"html_var": "hai,"
		}
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
 