from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["number_auto", "description", "status"]
        widgets = {
            "number_auto": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер'
        }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
            ,  "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите из списка'
            })
        }
