from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from menus.models import Menus


@register(Menus)
class MenusAdmin(admin.ModelAdmin):
    list_display = ('name',)
