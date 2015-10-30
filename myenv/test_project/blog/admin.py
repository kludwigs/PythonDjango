from django.contrib import admin

#app name and models and select the class to import from
from blog.models import MyBlog
# Register your models here.
admin.site.register(MyBlog)