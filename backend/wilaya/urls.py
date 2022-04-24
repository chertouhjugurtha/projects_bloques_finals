from django.urls import path
from wilaya import views

urlpatterns = [
    path('wilaya/insertion/', views.WilayaViewSet.as_view()),
    path('wilaya/modification/<code_wilaya>/', views.WilayaViewSet.as_view()),
    path('wilaya/suppression/<code_wilaya>/', views.WilayaViewSet.as_view()),
    path('get_wilaya/', views.get_wilaya),
]