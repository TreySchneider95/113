from django.urls import path, include
from .views import AddArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('add', AddArticleView.as_view(), name='add_article'),
    path('edit/<pk>', UpdateArticleView.as_view(), name='edit_article'),
    path('delete/<pk>', DeleteArticleView.as_view(), name='delete_article'),
]