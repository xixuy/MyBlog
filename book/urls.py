from django.urls import path
from . import views


urlpatterns=[
    path('index/',views.index),
    path('add_book/',views.add_book),
    path('book_detail/',views.book_detail),
]