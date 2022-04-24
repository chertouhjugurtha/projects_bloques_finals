
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('wilaya.urls')),
    path('api/', include('commune.urls')),
    path('api/', include('gerant.urls')),
    path('api/', include('entreprise.urls')),
    path('api/', include('branche.urls')),
    path('api/', include('activite.urls')),
    path('api/', include('projets.urls')),
    path('api/', include('motifs.urls')),
    path('api/', include('observation.urls')),
    path('api/', include('debloqueur.urls')),
    path('api/', include('ministere.urls')),
   
    
  


]
