from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from recipe.models import Recipe


@register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
