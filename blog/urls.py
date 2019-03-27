from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('login.html',views.login),
    path('product/',views.product),
    path('model/<int:id>/',views.model_index)
]
