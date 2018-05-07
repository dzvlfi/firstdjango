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
	rand = random.randint(0, 1000)
	return render(request, 'base.html', {"html_var": "context", "num": rand}) #response, with context