from rest_framework import serializers

from menus.models import Menus
from recipe.serializers import RecipeSerializer


class MenusSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(read_only=True, many=True)

    class Meta:
        model = Menus
        fields = ('id', 'name', 'recipes')


class MenusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ('id', 'name', 'recipes')
