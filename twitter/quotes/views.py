# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

def index(request):
	return render(request, 'quotes/index.html')


def web(request):
	channel = request.GET.get('txtSearch')
	url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=6740eb210d73469b9d9695041ff4b406'
	
	r=requests.get(url.format(channel)).json()

	news = {
	'url':r['articles'][0]['url'],
	'author':r['articles'][0]['author'],
	}
       
	print news

        context = {'news':news}
    
	return render (request, 'quotes/main.html',context)