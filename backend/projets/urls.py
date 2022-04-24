from django.urls import path
from projets import views

urlpatterns = [
    path('projets/insertion/', views.ProjetsViewSet.as_view()),
    path('projets/modification/<uuid:pk>/', views.ProjetsViewSet.as_view()),
    path('projets/suppression/<uuid:pk>/', views.ProjetsViewSet.as_view()),
    
]