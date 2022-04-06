from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
from datetime import datetime


class Category(ListView):
    model = PostCategory
    template_name = 'news.html'
    context_object_name = 'category'


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-time_add_post')


class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news_text.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет
#