from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'release_year', 'content', 'poster_url', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }