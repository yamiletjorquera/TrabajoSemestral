from django.contrib import admin
from .models import User, Author, Book
# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)