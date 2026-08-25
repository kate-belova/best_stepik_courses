from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from courses.sitemaps import StaticViewSitemap, CourseSitemap
from courses.views import courses_list, course_detail
from suggestions.views import suggestion_create

sitemaps = {
    "static": StaticViewSitemap,
    "courses": CourseSitemap,
}
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", courses_list, name="courses_list"),
    path(
        "suggest-course/",
        suggestion_create,
        name="suggestion_create",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "<slug:course_slug>/",
        course_detail,
        name="course_detail",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
