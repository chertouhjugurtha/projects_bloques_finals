from django.urls import path
from gerant import views

urlpatterns = [
    path('gerant/insertion/', views.GerantViewSet.as_view()),
    path('gerant/modification/<uuid:pk>/', views.GerantViewSet.as_view()),
    path('gerant/suppression/<uuid:pk>/', views.GerantViewSet.as_view()),
    
]