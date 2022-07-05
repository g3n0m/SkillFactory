from django.forms import DateInput, SelectDateWidget
from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Post
 

class PostFilter(FilterSet):
    post_date = DateFromToRangeFilter(label='Временной интервал', widget=RangeWidget(attrs={'type': 'date'}))
    
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }
