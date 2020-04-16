from django.urls import path
from .views import PostagemCreate
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('add', PostagemCreate.as_view(), name= 'add_post'),
    path('login/', auth_views.LoginView.as_view(), name='login')

]