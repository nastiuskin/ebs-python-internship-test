from django.contrib import admin

from apps.blog.models import Blog, Category, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
   list_display = ('title', 'enabled')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
