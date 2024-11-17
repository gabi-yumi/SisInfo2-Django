from django.contrib import admin
from books.models import Category, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
