from django.contrib import admin
from django.urls import include, path
from apps.core.custom_router import router


urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('apps.accounts.urls')),  # without namespace
    path('admin/', admin.site.urls),
] + router.urlpatterns
