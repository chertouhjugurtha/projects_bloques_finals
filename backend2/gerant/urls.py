from django.urls import path
from ministere import views

urlpatterns = [
    path('gerant/insertion', views.MinistereViewSet.as_view()),
]