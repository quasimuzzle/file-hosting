from django import forms
from .models import File, Comment

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'description', 'file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        