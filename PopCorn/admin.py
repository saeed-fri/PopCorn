from django.contrib import admin

#from blog.models import Blog, Author, Entry
from .models import Users

admin.site.register(Users)