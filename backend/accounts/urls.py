
from django.urls import path,include
from branche import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    
]