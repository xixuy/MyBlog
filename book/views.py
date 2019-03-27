from django.db import connection
from django.shortcuts import render

# Create your views here.

def get_corsor():
    return connection.cursor()


def index(request):
    # cursor=get_corsor()
    # cursor.execute("select id,book,name from book")
    # books=cursor.fetchall()

    return render(request,'book_index.html')


def add_book(request):
    return render(request, 'add_book.html')


def book_detail(request):
    return render(request,'book_detail.html')