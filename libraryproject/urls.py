from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions          # new
from drf_yasg.views import get_schema_view      # new
from drf_yasg import openapi                    # new



schema_view = get_schema_view(
    openapi.Info(
        title = "Book List Api",
        default_version = "v1",
        description = "Library demo project",
        terms_of_service = "demo.com",
        contact = openapi.Contact(name="Nozimjon",email="nozimjonhamdamov28@gmail.com"),
        license = openapi.License(name="Demo Licence")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('libraryapp.urls')),
    path('api-auth/', include('rest_framework.urls')),              # new
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),   # new
    
    #swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'
    )
]
