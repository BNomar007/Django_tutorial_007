from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Recipe, RecipeIngredient

User = get_user_model

admin.site.register(RecipeIngredient)

class UserInline(admin.TabularInline):
    model = User

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields = ['name', 'quantity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [UserInline, RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)
