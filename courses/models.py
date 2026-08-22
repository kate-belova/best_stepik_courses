from decimal import Decimal
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        "Название",
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        "Имя",
        max_length=50,
    )

    url = models.URLField(
        "Ссылка на автора",
        blank=True,
    )

    description = models.TextField(
        "Описание",
        blank=True,
    )

    avatar = models.ImageField("Фотография", upload_to="authors/photos/", blank=True)

    @property
    def initials(self):
        words = self.name.split()

        if not words:
            return "?"

        return "".join(word[0].upper() for word in words[:2])

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    categories = models.ManyToManyField(
        Category,
        verbose_name="Категории",
    )
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField("Slug", max_length=130, blank=True)
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    description = models.TextField("Описание")
    url = models.URLField("Ссылка на курс")
    price = models.DecimalField("Цена", max_digits=7, decimal_places=2, default=0)
    is_free = models.BooleanField("Бесплатный курс", default=False)
    image = models.ImageField("Фотография", upload_to="courses/photos/", blank=True)

    @property
    def display_price(self):
        if self.price == Decimal():
            return "Бесплатно"

        if self.price == self.price.to_integral():
            return f"{int(self.price):,} ₽".replace(",", " ")

        return f"{self.price} ₽"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["title"]

    def __str__(self):
        return self.title
