from django.contrib import admin

from courses.models import Course, Category, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "is_free"]
    filter_horizontal = ["categories", "authors"]
