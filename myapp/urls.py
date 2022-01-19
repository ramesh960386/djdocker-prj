from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.getdata, name='getdata')
]