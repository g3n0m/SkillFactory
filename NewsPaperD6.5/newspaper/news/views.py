from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post as PostModel
from .filters import PostFilter
from .forms import PostForm
from .models import Category


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
