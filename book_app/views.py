from django.shortcuts import render, get_object_or_404,redirect
from.forms import AuthorForm,BookForm
from django.core.paginator import Paginator, EmptyPage
from .models import Book
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.

from .models import Book,Author

# def creatBook(request):

#     if request.method=='POST':

#         title=request.POST.get('title')
#         price=request.POST.get('price')

#         book=Book(title=title,price=price)

#         book.save()

#         return redirect('listview')  # Redirect to the list view after creating the book

#     books = Book.objects.all()
#     return render(request, 'book.html', {'books': books})

    

def listBook(request):
    books = Book.objects.all()
    if not books:
        print("No books found.")  # This will help debug if no books are found
    else:
        print(f"Books found: {books}")

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)




    return render(request, 'admin/listbook.html', {'books': books, 'page':page})

def detailsview(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detailsview.html', {'book': book})

def updateBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('listview')
    else:
        form = BookForm(instance=book)
    return render(request, 'admin/updateview.html', {'form': form})

def deleteview(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('listview')
    return render(request, 'admin/deleteview.html', {'book': book})

def creatBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listview')  # Redirect to the book list view after successful creation
    else:
        form = BookForm()
    
    books = Book.objects.all()  # Fetch all books
    return render(request, 'admin/book.html', {'form': form, 'books': books})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listview')
    else:
        form = AuthorForm()
    return render(request, 'admin/author.html', {'form': form})

def index(request):
    return render(request,'admin/base.html')

def Search_book(request):

    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query) )

    else:
        books=[] 

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)  

