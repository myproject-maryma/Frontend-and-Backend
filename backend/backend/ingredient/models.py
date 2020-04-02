from django.db import models

# Create your models here.
from recipe.models import Recipe


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ingredient_category'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.PositiveIntegerField(default = 999)
    recipes = models.ManyToManyField(Recipe, related_name='ingredients', blank=True)

    class Meta:
        db_table = 'ingredient'

    def __str__(self):
        return self.name
