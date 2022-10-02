from django.shortcuts import render

# Create your views here.
def mani5(request):
    return render(request,'mani.html',context={'name':'suman'})