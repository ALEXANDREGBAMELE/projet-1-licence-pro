from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def article(request):
    return render(request,'footer.html')

def contact(request):
    return render(request,'contact.html')

