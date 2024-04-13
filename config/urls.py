from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from books import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kitoblar do'koni API",
        default_version='v1',
        description="list Api Test BOOK",
        terms_of_service="local_host.com",
        contact=openapi.Contact(email='brawlstars7471255@gmail.com'),
        license=openapi.License(name="Demo License Test"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # local apps
    path('admin/', admin.site.urls),
    path("api/v1/", include('books.urls')),
    path('', views.Index.as_view()),
    # authcation and alauth
    path('/api/v1/dj-rest-auth/registration/account-confirm-email/',views.Index.as_view()),
    path('api/auth', include('rest_framework.urls')),
    # path('api/v1/dj-rest-auth/login/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # swagger and redoc
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')
]
