from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.category_detail, name='category-detail'),
    path('<slug:category_slug>/<slug:slug>/', views.book_detail, name='book-detail'),

]