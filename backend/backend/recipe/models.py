from django.db import models

from menus.models import Menus


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=128, null=True, blank=True)
    menus = models.ManyToManyField(Menus, related_name='recipes', blank=True)

    class Meta:
        db_table = 'recipe'

    def __str__(self):
        return self.name
