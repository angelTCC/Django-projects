from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import InputForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    fields = [field.name for field in Book._meta.get_fields()]
    form = InputForm()

    if request.method == "POST":
        edit_book = request.POST.get('edit_book')
        edit_book = int(edit_book)
    else:
        edit_book = 0
    
    return render(request, 'crud_operations.html', {'books': books, 'fields': fields, 'edit_book': edit_book, 'form':form})


def book_create(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    books = Book.objects.all()
    edit_book = None
    fields = [field.name for field in Book._meta.get_fields()]
    return render(request, 'crud_operations.html', {'books':books, 'fields':fields, 'edit_book':edit_book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
    return redirect('list')


def book_edit(request, book_id):
    books = Book.objects.all()
    edit_book = books.get(id=book_id)
    
    if request.method == 'POST':
        edit_book.title = request.POST['title']
        edit_book.author = request.POST['author']
        edit_book.published_date = request.POST['published_date']
        edit_book.description = request.POST['description']
        edit_book.save()
        return redirect('list')
    
    return redirect('list')
