from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from .forms import EditProfileForm, ProfilePageForm
from theboard.models import UserProfile, Post, User


class CreateProfilePageView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = "registration/edit_profile_page.html"
    fields = ['profile_pic', 'bio', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url', 'news_susbscribed']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(UpdateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

    def get_success_url(self):
        return reverse_lazy('show_profile_page', kwargs={'pk': self.kwargs['pk']})


class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, user_id=self.kwargs['pk'])
        cat_menu = Post.get_categories()
        context['cat_menu'] = cat_menu
        context['page_user'] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):    
    form_class = PasswordChangeForm 
    success_url = reverse_lazy('password_sucsess')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(PasswordChangeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    

def password_sucsess(request):
    return render(request, 'registration/password_sucsess.html', {})


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        cat_menu = Post.get_categories()
        context = super(UpdateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
