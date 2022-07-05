from django import forms
from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):   
    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'category': forms.Select(attrs={'class': 'form-control'}),            
            'body': forms.Textarea(attrs={'class': 'form-control'}),            
        }

    
class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'category': forms.Select(attrs={'class': 'form-control'}),       
            'body': forms.Textarea(attrs={'class': 'form-control'}),            
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Оставить коммент'}),
        }
