from django.shortcuts import render


def home(request):
		return render(request, 'home.html', {})

def about(request):
		from listapi.pyface import pyface
		return render(request, 'about.html', {"my_stuff": pyface})

def base(request):
		return render(request, 'base.html', {})

def charts(request):
		return render(request, 'charts.html', {})

def youtube(request):
		return render(request, 'youtube.html', {})

def learn(request):
		return render(request, 'learn.html', {})

def cards(request):
		return render(request, 'cards.html', {})


def welcome(request):
		return render(request, 'welcome.html', {})
