from django.shortcuts import render
from .models import Book, Review
from django.views.generic import ListView, DetailView
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "home.html"

class BookDetailView(DetailView): # new
    model = Book
    template_name = "book_detail.html"