from django.urls import path
from .views import PostagemCreate
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('add',PostagemCreate.as_view(), name= 'add_post')

]