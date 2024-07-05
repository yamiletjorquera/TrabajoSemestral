from django.contrib import admin
from .models import Usuario, Author, Book
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Author)
admin.site.register(Book)