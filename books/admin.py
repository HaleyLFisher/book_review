from django.contrib import admin
from .models import Book, Review
# Register your models here.

admin.site.register(Book)
admin.site.register(Review)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)