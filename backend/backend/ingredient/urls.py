from django.urls import path

from . import views

app_name = 'ingredient'

urlpatterns = [
    path('<int:id>/', views.IngredientRetrieveUpdateDeleteView.as_view()),

    path('', views.IngredientListCreateAPIView.as_view()),

]
