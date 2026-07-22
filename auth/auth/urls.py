from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title='Auth API',
        default_version='v1',
        description='API Documentation'
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
