from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('portfolio/', include('myportfolio.urls', namespace='portfolio')),
    path('blog/', include('posts.urls', namespace='blog')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
