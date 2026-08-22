from django.db import models


class Suggestion(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название курса",
    )
    url = models.URLField(
        verbose_name="Ссылка на курс",
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Ваше имя",
    )
    email = models.EmailField(
        blank=True,
        verbose_name="Ваш email",
    )
    telegram = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Ваш Telegram",
    )

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата отправки",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Предложение курса"
        verbose_name_plural = "Предложения курсов"
