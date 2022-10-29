from django.contrib import admin
from .models import Books, Author, Genre, Editor
# Register your models here.

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Editor)

