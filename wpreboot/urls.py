from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from wpreboot.feeds import TurboFeed
from wpreboot.sitemaps import BlogSitemap

from django.contrib.sitemaps import views

sitemaps = {
    'static': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls', namespace='blog')),
    path('feeds/turbo.xml', TurboFeed()),
    # the sitemap
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
