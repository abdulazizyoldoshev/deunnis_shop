from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']


@admin.register(BlogTagModel)
class BlodTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title', 'tags', 'description']
    autocomplete_fields = ['author', 'tags']
