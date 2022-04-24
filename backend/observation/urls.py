from django.urls import path
from observation import views

urlpatterns = [
    path('observation/insertion/', views.ObservationViewSet.as_view()),
    path('observation/modification/<uuid:pk>/', views.ObservationViewSet.as_view()),
    path('observation/suppression/<uuid:pk>/', views.ObservationViewSet.as_view()),
    
]