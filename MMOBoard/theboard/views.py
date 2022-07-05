from django.http import request, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Comment, User, UserProfile
from .forms import PostForm, EditForm, CommentForm
from .filters import PostFilter
from .tasks import subscribe_confirmation_message


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('article-detail', pk=comment.post.pk)
    

@login_required
def comment_disapprove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.disapprove()
    return redirect('article-detail', pk=comment.post.pk)
    

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('article-detail', pk=comment.post.pk)


@login_required
def news_subscribe(request, pk):
    userprofile = get_object_or_404(UserProfile, user_id=request.user.id)
    userprofile.subscribe()
    user_name = request.user.username 
    email = request.user.email
    subscribe_confirmation_message.delay(user_name, email)
    return redirect('home')


class HomeView(ListView):
    model = Post
    template_name = 'theboard/home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu        
        return context
    

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-post_date')
    cat_menu = Post.get_categories()
    return render(request, 'theboard/categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts, 'cat_menu': cat_menu})


class DashboardView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'theboard/dashboard.html'
    context_object_name = 'author_posts'
    ordering = ['-post_date']
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-post_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.request.user
        author_posts = Post.objects.filter(author=author).order_by('-post_date')
        cat_menu = Post.get_categories()
        context['cat_menu'] = cat_menu
        context['author_posts'] = author_posts
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theboard/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(DetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        post_comments = current_post.comments.order_by('-date_added')
        post_comments_count = current_post.comments.count()
               
        context['post_comments_count'] = post_comments_count
        context['post_comments'] = post_comments    
        context['cat_menu'] = cat_menu        
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theboard/add_post.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'theboard/add_comment.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'theboard/update_post.html'
    form_class = EditForm
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(UpdateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'theboard/delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
