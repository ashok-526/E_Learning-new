# E_Learning/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('Home.urls')),
    path('admin/', admin.site.urls),
]

# Only serve static and media files during development (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This line helps automatically serve files in STATICFILES_DIRS when DEBUG=True
urlpatterns += staticfiles_urlpatterns()
