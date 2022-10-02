from django.urls import path
from app5.views import *
app_name='anything'
urlpatterns =[
    path('suman/',suman,name='iam suman'),
]
