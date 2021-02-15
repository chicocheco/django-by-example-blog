from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    # there is no location method - by default, location() calls get_absolute_url() on each object

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):  # returns datetime
        return obj.updated
