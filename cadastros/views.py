from .models import Pessoas
from  django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.
class PessoasCreate(CreateView):
    model = Pessoas
    fields = ['codigo', 'nome', 'rg', 'expedidor', 'uf', 'cpf', 'titulo', 'nacionalidade', 'natural', 'estado_civil', 'qtd_dependentes', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado', 'celular1', 'celular2', 'e_mail' ]
    success_url = reverse_lazy('post_list')

class PessoasListView(ListView):
    model = Pessoas

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context