from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/edit', views.ArticleEditView.as_view(), name='article-edit'),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article-delete')

]