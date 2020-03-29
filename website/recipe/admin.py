from django.contrib import admin
from .models import Category, Recipe

admin.site.register(Category)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'chef')
    list_filter = ('category', 'chef')
    search_fields = ['title']

admin.site.register(Recipe, RecipeAdmin)

