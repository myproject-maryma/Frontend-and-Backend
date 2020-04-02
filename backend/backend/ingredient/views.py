from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer, IngredientListSerializer


class IngredientListCreateAPIView(ListCreateAPIView):
    serializer_class = IngredientSerializer
    list_serializer_class = IngredientListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.serializer_class

    def get_queryset(self):
        kwargs = {}
        category = self.request.GET.get('category')

        if category:
            kwargs['category__name'] = category
        return Ingredient.objects.filter(**kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

#Create  ingredient and retrieve ingredient list view
class IngredientRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientSerializer
    # permission_classes = (IsAuthenticated, DjangoModelPermissions)
    lookup_field = 'id'
    list_serializer_class = IngredientListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.serializer_class

    def get_queryset(self):
        return Ingredient.objects.filter()
