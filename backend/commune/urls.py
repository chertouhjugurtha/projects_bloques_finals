from django.urls import path
from commune import views

urlpatterns = [
    path('commune/insertion/', views.CommuneViewSet.as_view()),
    path('commune/modification/<uuid:pk>/', views.CommuneViewSet.as_view()),
    path('commune/suppression/<uuid:pk>/', views.CommuneViewSet.as_view()),
    path('get_commune/', views.get_commune),
]