from django.urls import path

from . import views

app_name = 'recipe'

urlpatterns = [

    path('<int:id>/', views.RecipeRetrieveUpdateDeleteView.as_view()),
    path('', views.RecipeListCreateAPIView.as_view()),

]
