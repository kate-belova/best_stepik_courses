from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Course


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["courses_list"]

    def location(self, item):
        return reverse(item)


class CourseSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return Course.objects.all()

    def location(self, item):
        return reverse(
            "course_detail",
            kwargs={"course_slug": item.slug},
        )
