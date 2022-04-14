from django.urls import path
from .views import NewsListView, NewsDetail, NewsSearchView
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view()),
    path('news/search/', NewsSearchView.as_view(), name='news_search'),
    path('news/add/', PostCreateView.as_view(), name='post_create'),
    path('news/<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('news/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]
