from django.urls import path
from . import views

urlpatterns = [
    path('showline/', views.showlinediagram,name='showline'),

]
