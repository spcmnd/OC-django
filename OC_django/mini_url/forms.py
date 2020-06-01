from django import forms
from .models import MiniURL


class URLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('url', 'author')

