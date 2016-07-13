from django import forms

from excel.models import Files


class FileForm(forms.Form):
    class Meta:
        model = Files
        fields = ('name', 'file')
