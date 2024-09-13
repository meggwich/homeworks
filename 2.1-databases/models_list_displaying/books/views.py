from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def books_view(request):
    books = Book.objects.all()
    return render(request, 'base.html', {'books': books})

# def list_books_by_date(request, pub_date):
#     books = Book.objects.filter(pub_date=pub_date)
#     previous_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
#     next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
#     return render(request, 'books/book_list.html', {
#         'books': books,
#         'previous_date': previous_date.pub_date if previous_date else None,
#         'next_date': next_date.pub_date if next_date else None,
#         'pub_date': pub_date
#     })
#
#
# from django.shortcuts import render
# from .models import Book


def list_books_by_date(request, pub_date):
    books = Book.objects.filter(pub_date=pub_date)
    previous_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'books': books,
        'previous_date': previous_date.pub_date if previous_date else None,
        'next_date': next_date.pub_date if next_date else None,
        'pub_date': pub_date
    }

    return render(request, 'book_list.html', context)


