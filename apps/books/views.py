from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from books.models import Book
from books.forms import BookForm

# ---para a API--- #
from rest_framework import generics
from .serializers import BookSerializer
# ---/para a API--- #


class BookListView(TemplateView):
    template_name = "book/livro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Book.objects.filter(user = self.request.user)
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/adicionar_livro.html'
    success_url = reverse_lazy("livros")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book/apaga_livro.html"
    success_url = reverse_lazy('livros')
    


# ---para a API--- #
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# ---/para a API--- #