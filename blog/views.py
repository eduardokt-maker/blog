from django.shortcuts import render
from .models import Postagem
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts= Postagem.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

    # return render(request, 'blog/post_list.html', {})




