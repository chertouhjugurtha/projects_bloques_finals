from django.urls import path
from motifs import views

urlpatterns = [
    path('motifs/insertion/', views.MotifsViewSet.as_view()),
    path('motifs/modification/<uuid:pk>/', views.MotifsViewSet.as_view()),
    path('motifs/suppression/<uuid:pk>/', views.MotifsViewSet.as_view()),
    
]