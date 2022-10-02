from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def suman(request):
    return HttpResponse('<h1>suman is diff person in the world</h1>')