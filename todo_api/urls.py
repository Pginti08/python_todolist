from django.conf import settings  # ✅ Add this import
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
# path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('products/', include('todo_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ✅ Serve media files
