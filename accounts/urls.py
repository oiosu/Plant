from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
    path('password/', views.change_pw, name='change_pw'),
    path('delete/', views.delete, name='delete'),
    # path('summernote/', include('django_summernote.urls')), 

]