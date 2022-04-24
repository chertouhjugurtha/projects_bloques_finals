from django.urls import path
from activite import views

urlpatterns = [
    path('activite/insertion/', views.ActiviteViewSet.as_view()),
    path('activite/modification/<uuid:pk>/', views.ActiviteViewSet.as_view()),
    path('activite/suppression/<uuid:pk>/', views.ActiviteViewSet.as_view()),
    # path('get_activite/', views.get_activite),
]