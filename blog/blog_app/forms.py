"""
Файл для создания Django-форм

<input type="text" placeholder="Title" name="title" >
<input type="text" placeholder="Content" name="content" >
<input type="checkbox" placeholder="is_publish" name="is_publish" >
<input type = "number" placeholder="author_id" name="author_id" >
"""
from django import forms
from django.forms.models import ModelForm

# Form - базовый класс для создания формы
# required=True - поле требуется
# required=False - по НЕ требуется (не обязательное)

# widget - аргумент с реальным полем на странице
# TextInput - <input type="text">
# EmailInput - <input type="email">
# FileInput - <input type="file">


class PostForm(forms.Form):

    title = forms.CharField(
        # Кирилл. Указать TextInput с атрибутом placehloder
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title"
            }
        ),
        max_length = 100,
        required = True)

    content = forms.CharField(
        # Миша Панков. УКазать TextInput, с плейхолдером
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Content"})
    )

    is_publish = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={ # attrs - атрибуты поля ввода
                "placeholder": "Is published" # placeholder="Is published",
            }
        ),
        label="is_publish"
    )

    author_id = forms.IntegerField(
        # Указать NumberInput, указать placeholder
        widget= forms.NumberInput(
            attrs= {
                "placeholder": "enter id"
            }
        ),
        required=False,
        min_value=1
    )
