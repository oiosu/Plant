from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.article_new, name="article_new"), #생성
    # add new url
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/new/', views.create_article, name='create_article'),
    path('articles/<int:article_id>/update/', views.update_article, name='update_article'),
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article')
]

