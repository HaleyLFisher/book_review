from django.shortcuts import render
from .models import Book, Review
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, FormView, View, CreateView, UpdateView, DeleteView
from .forms import ReviewForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "home.html"

class ReviewGet(DetailView): # new
    model = Book
    template_name = "book_detail.html"
    
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context

class BookDetailView(View): # new
    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)

class ReviewPost(SingleObjectMixin, FormView): # new
    model = Book
    form_class = ReviewForm
    template_name = "book_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.user = review.user
        review.save()
        return super().form_valid(form)
    def get_success_url(self):
        book = self.object
        return reverse("book_detail", kwargs={"pk": book.pk})

class BookCreateView(LoginRequiredMixin, CreateView): # new
    model = Book
    template_name = "book_new.html"
    fields = ["title", "author", "synopsis", "year_published"]
    

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = "book_update.html"
    fields = ["title", "author", "synopsis", "year_published"]
    permission_required = 'user.is_staff'
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("home")
    permission_required = 'user.is_staff'
    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user