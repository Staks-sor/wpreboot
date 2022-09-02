from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    limit = 1000

    def items(self):
        return Post.objects.all().order_by('-id')

    def location(self, item):
        return f'/post/id/{item.pk}'

    def lastmod(self, obj):
        return obj.date
