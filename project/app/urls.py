from .views import *
from django.urls import path
urlpatterns=[
    path('',set,name="set"),
    path('get/',get,name="get"),
    path('delete/',delete,name="delete"),
]