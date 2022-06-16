from django.urls import path, include
from .views import Posts, SearchPosts, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategorySubscribe, CategorySubscribe, subscribe_category, unsubscribe_category
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(Posts.as_view())),
    path('search/', SearchPosts.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('add/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('category/<int:pk>', cache_page(60*5)(CategorySubscribe.as_view()), name = 'post_category'),
    path('subscribe/<int:pk>', subscribe_category, name = 'subscribe_category'),
    path('unsubscribe/<int:pk>', unsubscribe_category, name='unsubscribe_category'),
]
