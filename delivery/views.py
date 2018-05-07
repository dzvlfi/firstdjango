from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home_old(request):
	html_var = 'aku' #f_strings
	html_ = f"""<!doctype html>
	<html lang="en">
	<head>
	</head>
	<body>
	<h1>Hello World!</h1>
	<p>{html_var} di bandung, dingin euy hehe</p>
	</body>
	</html>
	"""
	return HttpResponse(html_) 

def home(request):
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
		"some_list": some_list
	}
	return render(request, 'base.html', context) #response, with context