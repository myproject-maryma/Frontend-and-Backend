from django.urls import path

from . import views

app_name = 'menus'

urlpatterns = [
    path('pdf/', views.PDFMenus.as_view()),
    path('<int:id>/', views.MenusRetrieveUpdateDeleteView.as_view()),
    path('', views.MenusListCreateAPIView.as_view()),

]
