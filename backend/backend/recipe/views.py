from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer, RecipeCreateSerializer


class RecipeListCreateAPIView(ListCreateAPIView):
    serializer_class = RecipeSerializer
    create_serializer_class = RecipeCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class
        return self.serializer_class

    def get_queryset(self):
        # Recipe.objects.get(ingredients)

        kwargs = {}
        ingredient = self.request.GET.get('ingredient')
        category = self.request.GET.get('category')

        if ingredient:
            kwargs['ingredients__name__contains'] = ingredient
        if category:
            kwargs['ingredients__category__name'] = category
        return Recipe.objects.filter(**kwargs)

    def get_exact_match(self, model_class, m2m_field, ids):
        query = model_class.objects.annotate(count=Count(m2m_field)) \
            .filter(count=len(ids))
        for _id in ids:
            query = query.filter(**{m2m_field: _id})
        return query

    def perform_create(self, serializer):

        instance = serializer.save()
        return instance

    def create(self, request, *args, **kwargs):
        matches = self.get_exact_match(Recipe, 'ingredients', self.request.data['ingredients'])
        if matches:
            print('already exist')
            serializer = RecipeSerializer(matches[0])
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RecipeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    # permission_classes = (IsAuthenticated, DjangoModelPermissions)
    lookup_field = 'id'

    def get_queryset(self):
        return Recipe.objects.filter()
