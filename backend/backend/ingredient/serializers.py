from rest_framework import serializers

from ingredient.models import Ingredient, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class IngredientListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'category')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'category')
