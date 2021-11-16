from django.contrib import admin

from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] # change the display in the admin page
    search_fields = ['title', 'content'] # Add search bar in the admin page

admin.site.register(Article, ArticleAdmin)
