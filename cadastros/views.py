from .models import Pessoas
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class PessoasCreate(CreateView):
    model = Pessoas
    fields = ['codigo', 'nome', 'rg', 'expedidor', 'uf', 'cpf', 'titulo', 'nacionalidade', 'natural', 'estado_civil', 'qtd_dependentes', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado', 'celular1', 'celular2', 'e_mail' ]
    success_url = reverse_lazy('post_list')