from django_filters import FilterSet, filters
from django.forms.widgets import DateInput
from .models import Post, Category
from accounts.models import Author


class SearchNewsFilter(FilterSet):
    date = filters.DateFilter(
        field_name='create_time',
        label='Дата от:',
        lookup_expr='gte',
        widget=DateInput(attrs={'placeholder': 'ДД.ММ.ГГ'})
    )
    header = filters.CharFilter(
        field_name='header',
        label='Заголовок содержит:',
        lookup_expr='icontains',
    )
    author = filters.ModelChoiceFilter(
        field_name='author',
        label='Автор:',
        queryset=Author.objects.all()
    )

    class Meta:
        model = Post
        exclude = ['author', 'header', 'type', 'create_time', 'category', 'rating', 'text']
