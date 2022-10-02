from django.shortcuts import render

# Create your views here.
def sumn(request):
    return render(request,'manith.html',context = {'name':'suman','name1':'komali'})