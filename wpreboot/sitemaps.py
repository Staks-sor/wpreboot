from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    limit = 1000

    def items(self):
        return Post.objects.all().order_by('-id')

    def lastmod(self, obj):
        return obj.date
