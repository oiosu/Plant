from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("<int:pk>/follow/", views.follow, name="follow"),
    path("<int:pk>/", views.detail, name="detail"),
    path("signup/", views.signup, name="signup"),
    path("update/", views.update, name="update"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]