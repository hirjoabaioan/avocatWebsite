from django.contrib.sitemaps import Sitemap
from .models import Postări


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Postări.published.all()
    
    def lastmod(self, obj):
        return obj.updated