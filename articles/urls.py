from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"), #생성
    path("create/", views.create, name="create"), #생성
    path("detail/<int:pk>", views.detail, name="detail"), #내용보기
    path("edit/<int:pk>", views.edit, name="edit"), # 수정
    path("update/<int:pk>", views.update, name="update"), #수정
    path("delete/<int:pk>", views.delete, name="delete"),  # 삭제
]

