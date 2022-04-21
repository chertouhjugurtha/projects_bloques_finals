from django.urls import path
from ministere import views

urlpatterns = [
    path('ministere/insertion', views.MinistereViewSet.as_view()),
]