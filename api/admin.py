from django.contrib import admin

from .models import Category, Job, Comment

admin.site.register([Category, Job, Comment])
