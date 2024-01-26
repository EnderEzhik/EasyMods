from .models import Mod, Category
from django.forms import ModelForm, TextInput, Select, CheckboxSelectMultiple


class ModForm(ModelForm):
    class Meta:
        model = Mod
        fields = ["name", "url", "version", "categories"]

        widgets = {
            "name": TextInput(attrs={
                "placeholder": "Название"
            }),
            "url": TextInput(attrs={
                "placeholder": "Ссылка"
            }),
            "version": Select(attrs={
                "placeholder": "Версия"
            }),
            "categories": CheckboxSelectMultiple(attrs={
                "placeholder": "Категории"
            }, choices=Category)
        }