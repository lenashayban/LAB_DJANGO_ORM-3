from django import forms
from .models import Post

class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Content', 'publish_date', 'is_published']