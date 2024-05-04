from django import forms
from django.forms import TextInput, DateTimeInput, Textarea

from .models import Survey


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер анкеты'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Биография'
            }),
        }
