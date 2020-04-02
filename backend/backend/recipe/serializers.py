from rest_framework import serializers
from ingredient.serializers import IngredientSerializer

from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients')


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients')

    def validate(self, data):
        # check quantity
        error_list = []
        for ingredient in data['ingredients']:
            if ingredient.quantity == 0:
                print(ingredient.name)
                name = ingredient.name
                error_list.append("There is no more {0}(id:{1})".format(name, ingredient.id))

            else:
                pass
        # quantity -1
        if len(error_list) > 0:
            raise serializers.ValidationError(
                {'ingredients': error_list}
            )

        return data
