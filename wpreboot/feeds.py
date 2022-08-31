from yaturbo import YandexTurboFeed
from blog.models import Post

class TurboFeed(YandexTurboFeed):
    """
    More information on Django Syndication Feed Framework configuration:
    https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
    """

    turbo_sanitize = True  # Let's strip HTML tags unsupported by Turbo pages.

    def items(self):
        return Post.objects.all()

    def item_turbo(self, item):
        # By default Turbo contents is taken from `item_description`.
        # Here we take turbo page contents from `html` attribute of an item.
        # Since we have `turbo_sanitize = True`, our HTML will be sanitized
        # automatically.
        #
        # Take a note, that if we return falsy item would be considered
        # as not having turbo contents at all.
        #
        return item.get('html', '')

    # You can also override other item_turbo_* family members.
