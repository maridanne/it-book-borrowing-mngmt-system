from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from books.models import Book, Category
from transactions.models import Transaction
from .forms import BookForm, CategoryForm, TransactionForm, UpdateTransactionForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from userprofiles.models import Profile


def frontpage(request):
    return render(request, 'core/frontpage.html')

def browsebooks(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        return render(request, 'core/categories.html', {'categories':categories})
    else:
        return redirect('/accounts/login/')

def signinpage(request):
    return render(request, 'core/signin.html')

@login_required(login_url='signinpage')
def categories(request):
    categories = Category.objects.all()
    return render(request, 'core/categories.html', {'categories':categories})

def about(request):
    return render(request, 'core/about.html')


def add(request):
    return render(request, 'core/add.html')

def addbook(request): 
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            book = form.cleaned_data.get('title')
            messages.success(request, book + ' is successfully saved.')
            return redirect('/addbook/')

    return render(request, 'core/add_product.html', {'form' : form})

def addcategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category = form.cleaned_data.get('title')
            messages.success(request, category + ' category is successfully saved.')
            return redirect('/addcategory/')


    return render(request, 'core/addcategory.html', {'form' : form})


def updatebook(request, pk): #UPDATE
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            book = form.cleaned_data.get('title')
            messages.success(request, book + ' is successfully updated.')

    context ={
        'form' : form,
        'book' : book
    }

    return render(request, 'core/updatebook.html', context)

def deletebook(request, pk): #DELETE
    book = Book.objects.get(id=pk)
    book.delete()
    messages.success(request, 'The product recently selected was deleted successfully.')
    return render(request, 'core/deletemsg.html')

@login_required(login_url='signinpage')
def borrow(request, slug):
    book = Book.objects.get(slug=slug)
    fName = request.user.first_name
    lName = request.user.last_name
    current_user = fName + ' ' + lName
    form = TransactionForm(initial={'book': book.title, 'borrower': current_user})
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            transaction = form.cleaned_data.get('transaction_id')
            messages.success(request, 'Transaction ID:' + transaction + '. Successfully Requested.')
            return redirect('/request_confirmed/')
    context = {
        'form': form, 
        'book': book
        }
    return render(request, 'core/borrow_details.html', context)

def request_confirmed(request):
    return render(request, 'core/reqconf.html')

def transaction(request):
    if request.user.is_staff:
        transactions = Transaction.objects.all()
        return render(request, 'core/lib_transaction.html', {'transactions': transactions})
    else:
        fName = request.user.first_name
        lName = request.user.last_name
        current_user = fName + ' ' + lName
        transactions = Transaction.objects.filter(borrower=current_user)
        return render(request, 'core/stud_transaction.html', {'transactions': transactions})
    
from django.shortcuts import render, redirect
from transactions.models import Transaction

def uptrans(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    form = UpdateTransactionForm(instance=transaction)

    if request.method == 'POST':
        form = UpdateTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            transaction = form.cleaned_data.get('transaction_id')
            messages.success(request, transaction + ' is successfully updated.')

    context ={
        'form' : form,
        'transaction' : transaction
    }

    return render(request, 'core/uptrans.html', context)

def returned(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    transaction.date_returned = timezone.now()
    transaction.save()
    return redirect('/transaction/', transaction_id=transaction_id)

def search_trans(request):
    query = request.GET.get('query', '')
    transactions = Transaction.objects.filter(Q(transaction_id__contains=query) | Q(borrower__icontains=query))
    context = {
        'transactions': transactions,
        'query': query
    }
    return render(request, 'core/search_trans.html', context)

def viewprofile(request):
    return render(request, 'core/viewprofile.html')

@login_required
def editprofile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect('editprofile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'core/editprofile.html', {'form': form})
