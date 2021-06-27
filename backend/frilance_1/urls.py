from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import api_root


schema_view = get_schema_view(
   openapi.Info(
      title="FastPrepUsa API",
      default_version='v1',
      description="Description for API FastPrepUsa",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('', api_root, name='api-root'),
    path('pay_image/', include('apps.pay_image.urls')),
    path('service/', include('apps.service.urls')),
    path('social/', include('apps.social.urls')),
    path('tarif/', include('apps.tarif.urls')),
    path('linkprice/', include('apps.link.urls')),
    path('form/', include('apps.contact.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    path('api/', include(api_patterns)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += i18n_patterns(
    path('pay_image/', include('apps.pay_image.urls')),
    path('service/', include('apps.service.urls')),
    path('social/', include('apps.social.urls')),
    path('tarif/', include('apps.tarif.urls')),
    path('linkprice/', include('apps.link.urls')),
    path('form/', include('apps.contact.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

