from django import forms


class CourseFilterForm(forms.Form):
    PRICE_TYPE_CHOICES = [
        ("", "Все курсы"),
        ("free", "Бесплатные"),
        ("paid", "Платные"),
    ]

    min_price = forms.IntegerField(required=False, label="от")
    max_price = forms.IntegerField(required=False, label="до")
    price_type = forms.ChoiceField(
        required=False,
        choices=PRICE_TYPE_CHOICES,
        label="Тип",
    )

    query = forms.CharField(
        required=False,
        label="Категории или технологии",
        help_text="Несколько значений укажите через запятую",
        widget=forms.TextInput(attrs={"placeholder": "Python, Go, QA Automation..."}),
    )

    ORDERING_CHOICES = [
        ("title", "По алфавиту"),
        ("price", "По цене: от низкой к высокой"),
        ("-price", "По цене: от высокой к низкой"),
    ]
    ordering = forms.ChoiceField(
        required=False, label="Сортировка", choices=ORDERING_CHOICES
    )
