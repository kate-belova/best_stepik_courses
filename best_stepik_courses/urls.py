from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from courses.views import courses_list, course_detail
from suggestions.views import suggestion_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", courses_list, name="courses_list"),
    path(
        "suggest-course/",
        suggestion_create,
        name="suggestion_create",
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
