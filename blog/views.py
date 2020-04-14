from django.shortcuts import render
from .models import Postagem
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts= Postagem.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/post_list.html', {'poste':posts})

    # return render(request, 'blog/post_list.html', {})




