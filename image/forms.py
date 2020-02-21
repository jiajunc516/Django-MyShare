from django import forms
from .models import Image, Comment

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("title", "description", "image")

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("comment", )

class TagForm(forms.Form):
    tags = forms.CharField()