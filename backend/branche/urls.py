from django.urls import path
from branche import views

urlpatterns = [
    path('branche/insertion/', views.BrancheViewSet.as_view()),
    path('branche/modification/<uuid:pk>/', views.BrancheViewSet.as_view()),
    path('branche/suppression/<uuid:pk>/', views.BrancheViewSet.as_view()),
    # path('get_branche/', views.get_branche),
]