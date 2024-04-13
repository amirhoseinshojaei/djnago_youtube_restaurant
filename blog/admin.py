from django.contrib import admin
from .models import Blog , Category , Tag , Comments
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comments

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','published_at')
    list_filter = ['published_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title','published_at']
    list_filter = ['published_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at',"author","category")
    list_filter = ("author",)
    search_fields = ("title",)
    ordering = ('title',"author")
    date_hierarchy = "author__date_joined"
    list_select_related = ('author',)
    inlines = [CommentInline]
