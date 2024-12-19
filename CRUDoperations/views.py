from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    edit_book = None
    fields = [field.name for field in Book._meta.get_fields()]
    return render(request, 'crud_operations.html', {'books':books, 'fields':fields, 'edit_book':edit_book})

def book_create(request):

    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['date']
        description = request.POST['description']
        
        Book.objects.create(
                            title=title,
                            author=author,
                            published_date=published_date,
                            description=description)
        
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
    return render(request, 'crud_operations.html', {})


def book_edit(request, book_id):
    books = Book.objects.all()
    fields = [field.name for field in Book._meta.get_fields()]
    
    # Set edit_book if we're editing

    edit_book = books.get(id=book_id)
    print(edit_book.author)
    print(20*"+")


    if request.method == 'POST':
        # Update the book with new values
        print(20*"+")
        print(request.POST['title'])
        print(20*"+")

        edit_book.title = request.POST['title']
        edit_book.author = request.POST['author']
        edit_book.published_date = request.POST['published_date']
        edit_book.description = request.POST['description']
        edit_book.save()  # Save the changes to the database
        
        return redirect('list')  # Redirect to the list view after saving
    

    return render(request, 'crud_operations.html', {
        'books': books,
        'fields': fields,
        'edit_book': edit_book
    })
