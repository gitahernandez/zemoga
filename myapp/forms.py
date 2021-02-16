from django import forms
from django.core.validators import FileExtensionValidator

class FileForm(forms.Form):
    docfile = forms.FileField(label='Select file', validators=[FileExtensionValidator(['csv'])])
