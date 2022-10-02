from django.shortcuts import render

# Create your views here.
def man(request):
    return render(request,'komali.html',context={'name':'kutty','working':'python developer'})