from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.frontpage, name='frontpage'),
    path('browsebooks', views.browsebooks, name='browsebooks'),
    path('categories/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('addbook/', views.addbook, name='addbook'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('updatebook/<pk>/', views.updatebook, name='updatebook'),
    path('deletebook/<pk>/', views.deletebook, name='deletebook'),
    path('borrow/<slug>', views.borrow, name='borrow'),
    path('request_confirmed/', views.request_confirmed, name='request_confirmed'),
    path('transaction/', views.transaction, name='transaction'),
    path('signinpage/', views.signinpage, name='signinpage'),
    path('uptrans/<transaction_id>/', views.uptrans, name='uptrans'),
    path('returned/<transaction_id>/', views.returned, name='returned'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('search_trans/', views.search_trans, name='search_trans'),
    path('', include('books.urls')),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
