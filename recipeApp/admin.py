from django.contrib import admin
from .models import Recipes

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cooking_time', 'created_at']
# Register your models here.
admin.site.register(Recipes, RecipeAdmin)
