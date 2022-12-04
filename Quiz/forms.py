from django.forms import ModelForm
from django import forms
from .models import QuesModel

class UploadForm(ModelForm):
    question=forms.TextInput()
    op2=forms.TextInput()
    op3=forms.TextInput()
    op4=forms.TextInput()
    ans=forms.TextInput()
    class Meta:
        model=QuesModel
        fields='__all__'
