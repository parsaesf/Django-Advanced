from django.contrib import admin
from .models import Post,Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'author', 'created_date', 'published_date', ]
    list_filter = ['author', 'status',]
    search_fields = ['title']


admin.site.register(Category)