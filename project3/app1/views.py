from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def app_mani6(request):
    return HttpResponse('<h1><marquee>iam mani</marquee></h1>')
def app_mani7(request):
    return HttpResponse('<i>iam mani1</i>')
def app_mani8(request):
    return HttpResponse('<h2>iam mani</h2>')
def app_mani9(request):
    return HttpResponse('<h3>iam mani1</h3>')
def app_mani10(request):
    return HttpResponse('<h4>iam mani1</h4>')