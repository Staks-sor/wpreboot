from django.utils.feedgenerator import Rss201rev2Feed
from yaturbo import YandexTurboFeed

from blog.models import Post
from yaturbo import YandexTurboFeed

from blog.models import Post


class iTunesFeed(Rss201rev2Feed):
    content_type = 'application/xml; charset=utf-8'

    def root_attributes(self):
        attrs = super().root_attributes()
        attrs['xmlns:itunes'] = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
        return attrs


class TurboFeed(YandexTurboFeed):
    link = '/post/'
    content_type = 'application/xml; charset=utf-8'
    feed_type = iTunesFeed

    turbo_sanitize = True  # Let's strip HTML tags unsupported by Turbo pages.

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
    def item_turbo(self, item) -> str:
        return item.content
    # item_link is only needed if NewsItem has no get_absolute_url method.
