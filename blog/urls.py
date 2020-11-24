from django.urls import path
from django.conf.urls import url
from .views import inicio

urlpatterns = [
     path('index/', inicio, name='index'),

]