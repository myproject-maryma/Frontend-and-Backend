from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from ingredient.models import Ingredient, Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
