from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

