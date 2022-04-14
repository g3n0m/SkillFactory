from django import forms

from .models import Post, Category
from accounts.models import Author


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label='Автор:',
    )
    type = forms.ChoiceField(
        choices=Post.TYPE,
        label='Тип записи:'
    )
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
    )
    header = forms.CharField(
        label='Заголовок',
    )
    text = forms.CharField(
        label='Текст записи',
        widget=forms.Textarea()
    )

    class Meta:
        model = Post
        fields = ['author', 'type', 'category', 'header', 'text']
