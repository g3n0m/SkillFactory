from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.cache import cache

from .models import Post as PostModel
from .filters import PostFilter
from .forms import PostForm
from .models import Category
from .tasks import send_new_mail

import logging

class Posts(ListView):
    model = PostModel
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-datetime']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        console_1 = logging.getLogger('console_1')
        console_1.debug("")
        console_1.info("")
        console_2 = logging.getLogger('console_2')
        console_2.warning("")
        console_3 = logging.getLogger('console_3')
        console_3.error("")
        console_3.critical("")
        file = logging.getLogger('file')
        file.info("")
        file.warning("")
        file.error("")
        file.critical("")
        django_request = logging.getLogger('django.request')
        django_request.error("")
        django_request.critical("")
        django_server = logging.getLogger('django.server')
        django_server.error("")
        django_server.critical("")
        django_template = logging.getLogger('django.template')
        django_template.error("")
        django_template.critical("")
        django_db = logging.getLogger('django.db_backends')
        django_db.error("")
        django_db.critical("")
        file_3 = logging.getLogger('file_3')
        file_3.debug("")
        file_3.info("")
        file_3.warning("")
        file_3.error("")
        file_3.critical("")

        return super().get(request, *args, **kwargs)


class SearchPosts(ListView):
    model = PostModel
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-datetime']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

 
class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'news/post_detail.html'
    queryset = PostModel.objects.all()

    def get_object(self, *args, **kwargs):
        obj=cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(*args, **kwargs) 
            cache.set(f'product-{self.kwargs["pk"]}', obj)
        
        return obj


class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = PostModel
    fields = '__all__'
    template_name = 'news/post_create.html'
    from_class = PostForm
    permission_required = ('news.add_Post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


class PostUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name='news/post_create.html'
    form_class = PostForm
    permission_required = ('news.change_Post')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return PostModel.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name='news/post_delete.html'
    queryset=PostModel.objects.all()
    success_url='/news/'

class CategorySubscribe(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'news/post_category.html'
    context_object_name = 'post_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def subscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    
    return redirect('/news')

@login_required
def unsubscribe_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    return redirect('/news')


def send_mail(instance):
    sub_text = instance.main_part

    for category in instance.postCategories.all():
        for subscriber in category.subscribers.all():
            html_content = render_to_string(
                'news/mail.html', {'post': instance, 'text': sub_text[:50], 'category': category.article_text})

            username = subscriber.username
            email = subscriber.email

            send_new_mail.delay(username, email, html_content)

        return redirect('/news/')
