from django.contrib import admin
from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'pub_date',)
    list_filter = ['pub_date',
                   'author'
                   ]


# admin.site.register(Book, BookAdmin)
