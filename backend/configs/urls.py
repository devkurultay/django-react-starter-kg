from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Developers' Kurultay")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('sw/', schema_view),

]
