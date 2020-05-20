from django.shortcuts import render
from .models import Postagem
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



# Create your views here.

def post_list(request):
    posts= Postagem.objects.filter(data_pedido__lte=timezone.now()).order_by('data_pedido')
    return render(request, 'blog/post_list.html', {'poste':posts})

    # return render(request, 'blog/post_list.html', {})



class PostagemCreate(CreateView):
    model = Postagem
    fields = ['Produto', 'descricao', 'observacao', 'data_pedido', 'data_entrega']
    success_url = reverse_lazy('post_list')




