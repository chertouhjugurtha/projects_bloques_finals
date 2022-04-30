
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Djoser API",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(
        r"^api/v1/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    # path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.jwt')),

    path('api/', include('utilisateurs.urls')),
    path('api/', include('wilaya.urls')),
    path('api/', include('commune.urls')),
    path('api/', include('gerant.urls')),
    path('api/', include('entreprise.urls')),
    path('api/', include('branche.urls')),
    path('api/', include('activite.urls')),
    path('api/', include('projets.urls')),
    path('api/', include('motifs.urls')),
    path('api/', include('observation.urls')),
    # path("api/v1/", include("accounts.urls")),
    # path('api/v1/', include('debloqueur.urls')),
    path('api/', include('ministere.urls')),

]
