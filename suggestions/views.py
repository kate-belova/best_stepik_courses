from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from suggestions.forms import SuggestionForm


def suggestion_create(request):
    form = SuggestionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        suggestion = form.save()

        message = f"""
Новое предложение курса

Название: {suggestion.title}
Ссылка: {suggestion.url}
Комментарий: {suggestion.comment or "Не указан"}

Имя: {suggestion.name or "Не указано"}
Email: {suggestion.email or "Не указан"}
Telegram: {suggestion.telegram or "Не указан"}
"""

        send_mail(
            subject=f"Новый курс: {suggestion.title}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_RECEIVER],
        )

        url = reverse("suggestion_create")
        return HttpResponseRedirect(f"{url}?sent=1")

    sent = "sent" in request.GET

    return render(
        request,
        "suggestions/suggestion_form.html",
        {
            "form": form,
            "sent": sent,
        },
    )
