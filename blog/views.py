from django.shortcuts import render, redirect
from .models import Postagem
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.urls import reverse_lazy


# Create your views here.

def post_list(request):
    posts= Postagem.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'poste':posts})

    # return render(request, 'blog/post_list.html', {})

class PostagemCreate(CreateView):
    model = Postagem
    fields = ['autor', 'titulo', 'texto', 'data_criacao', 'data_publicacao']
    success_url = reverse_lazy('post_list')



