from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'datetime', 'postAuthor', 'rating', 'main_part')
    list_filter = ('datetime', 'rating', 'postAuthor')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'rating')
    list_filter = ('authorUser', 'rating')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentUser', 'comment_text', 'datetime', 'rating')
    list_filter = ('commentUser', 'comment_text', 'datetime', 'rating')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)