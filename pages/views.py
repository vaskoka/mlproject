from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello this is the first page</h1>"),
   
