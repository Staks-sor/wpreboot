from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import views
from blog.views import PostSitemap
from wpreboot.feeds import TurboFeed

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('', include('blog.urls', namespace='blog')),
                  path('custom-sitemap.xml', views.sitemap.as_view(),
                       {'sitemaps': sitemaps, 'template_name': 'custom_sitemap.html'},
                       name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
