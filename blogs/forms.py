from django import forms
from .models import Blogpost


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
