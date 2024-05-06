from django.db.models import Q
from django.shortcuts import render
from .models import Book, Category


# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(Q(title__contains=query) | Q(author__icontains=query))
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'books/search.html', context)

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    books = category.books.all()
    context = {
        'category': category,
        'books': books
    }
    return render(request, 'books/category_detail.html', context)

def book_detail(request, category_slug, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})
