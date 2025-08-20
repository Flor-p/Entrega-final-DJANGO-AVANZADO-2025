from django.contrib import sitemaps
from django.urls import reverse

class VistapreviaSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        # Coincide con el name="index" de mi urls.py
        return ["index"]

    def location(self, item):
        return reverse(item)
