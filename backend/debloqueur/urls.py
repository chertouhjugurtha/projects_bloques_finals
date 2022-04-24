from django.urls import path
from debloqueur import views

urlpatterns = [
    path('debloqueur/insertion/', views.DebloqueurViewSet.as_view()),
    path('debloqueur/modification/<uuid:pk>/', views.DebloqueurViewSet.as_view()),
    path('debloqueur/suppression/<uuid:pk>/', views.DebloqueurViewSet.as_view()),
   
]