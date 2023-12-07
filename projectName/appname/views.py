from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'appname/home.html')

def about(request):
    return render(request, 'appname/about.html')

def contacts(request):
    return render(request, 'appname/contacts.html')

def codepractice(request):
    name = "MD. ABDUL KADER"
    country = "Bangladesh"
    skills = ["Python", "Django", "HTML"]
    data = {"name": name, "country": country, "skills": skills}
    return render(request, 'appname/codepractice.html', data)

def marketplace(request):
    return render(request, 'appname/marketplace.html')


