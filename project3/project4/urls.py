"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2.views import *
from app1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_mani/',app_mani,name='manith'),
    path('app_mani1/',app_mani1,name='manith'),
    path('app_mani2/',app_mani2,name='manith'),
    path('app_mani3/',app_mani3,name='manith'),
    path('app_mani4/',app_mani4,name='manith'),
    path('app_mani6/',app_mani,name='manith'),
    path('app_mani7/',app_mani1,name='manith'),
    path('app_mani8/',app_mani2,name='manith'),
    path('app_mani9/',app_mani3,name='manith'),
    path('app_mani10/',app_mani4,name='manith'),


]
