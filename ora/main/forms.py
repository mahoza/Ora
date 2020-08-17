from .models import Text
from .models import Login
from django.forms import ModelForm, TextInput, Textarea


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            })
        }


