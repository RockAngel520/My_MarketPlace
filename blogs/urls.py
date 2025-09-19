from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogsListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]