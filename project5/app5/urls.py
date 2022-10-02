from django.urls import path
from app5.views import *
app_name='you give anything'

urlpatterns =[
    path('suma/',suma,name='anything'),
]