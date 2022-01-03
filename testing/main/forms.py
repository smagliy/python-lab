from .models import TableHello
from django.forms import ModelForm, TextInput


class TableHelloForm(ModelForm):
    class Meta:
        model = TableHello
        fields = ['name', 'surname']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ім'я"
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Прізвище"
            })
        }