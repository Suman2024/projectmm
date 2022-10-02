from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_mani(request):
    return HttpResponse('<h1><marquee>iam mani</marquee></h1>')
def app_mani1(request):
    return HttpResponse('<i>iam mani1</i>')
def app_mani2(request):
    return HttpResponse('<h2>iam mani</h2>')
def app_mani3(request):
    return HttpResponse('<h3>iam mani1</h3>')
def app_mani4(request):
    return HttpResponse('<h4>iam mani1</h4>')