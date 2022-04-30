from django.urls import path
from entreprise import views

urlpatterns = [
    path('entreprise/insertion/', views.EntrepriseViewSet.as_view()),
    path('entreprise/modification/<uuid:pk>/', views.EntrepriseViewSet.as_view()),
    path('entreprise/suppression/<uuid:pk>/', views.EntrepriseViewSet.as_view()),
    # path('get_wilaya/', views.get_wilaya),
]