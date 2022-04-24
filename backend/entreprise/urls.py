from django.urls import path
from wilaya import views

urlpatterns = [
    path('entreprise/insertion/', views.WilayaViewSet.as_view()),
    path('entreprise/modification/<uuid:pk>/', views.WilayaViewSet.as_view()),
    path('entreprise/suppression/<uuid:pk>/', views.WilayaViewSet.as_view()),
    path('get_wilaya/', views.get_wilaya),
]