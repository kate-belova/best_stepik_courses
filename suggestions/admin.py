from django.contrib import admin

from suggestions.models import Suggestion


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "comment", "name", "email", "telegram", "date"]
