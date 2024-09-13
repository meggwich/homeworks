"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import books_view, list_books_by_date
from django.urls import path, register_converter
from books.converters import DateConverter

register_converter(DateConverter, 'yyyy')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books_view'),
    path('books/<yyyy:pub_date>/', list_books_by_date, name='list_books_by_date'),

]
