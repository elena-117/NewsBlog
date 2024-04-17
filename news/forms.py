from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea, TimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'preview', 'full_text', 'date', 'time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article name'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preview'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            }),
            'date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'time': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Time'
            }),
        }