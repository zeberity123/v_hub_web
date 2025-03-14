from django import forms
from .models import Asset

class AssetUploadForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['title', 'description', 'file', 'price']
