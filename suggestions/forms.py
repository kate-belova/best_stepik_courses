from django import forms

from suggestions.models import Suggestion


class SuggestionForm(forms.ModelForm):
    personal_data = forms.BooleanField(
        required=False,
        label="Даю согласие на обработку персональных данных",
    )

    class Meta:
        model = Suggestion
        fields = ["title", "url", "comment", "name", "email", "telegram"]

        error_messages = {
            "title": {
                "required": "Обязательное поле",
            },
            "url": {
                "required": "Обязательное поле",
            },
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Название курса",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "placeholder": "https://stepik.org/course/...",
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "placeholder": "Почему вы рекомендуете этот курс?",
                    "rows": 5,
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Ваше имя",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "example@mail.ru",
                }
            ),
            "telegram": forms.TextInput(
                attrs={
                    "placeholder": "@username",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean() or {}

        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        telegram = cleaned_data.get("telegram")
        personal_data = cleaned_data.get("personal_data")

        has_personal_data = name or email or telegram

        if has_personal_data and not personal_data:
            self.add_error(
                "personal_data",
                "Необходимо дать согласие на обработку персональных данных.",
            )

        return cleaned_data
