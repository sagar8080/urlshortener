from django import forms
from .models import Url

class ShortenUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']