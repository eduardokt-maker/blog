from django.conf import settings
from django.db import models
from django.utils import timezone
from produtos.models import Produtos






# Create your models here.



class Postagem(models.Model):
    titulo = models.CharField(max_length=100, null=True,blank=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    observacao = models.TextField()
    data_pedido = models.DateTimeField(default=timezone.now)
    data_entrega = models.DateTimeField(blank=True, null=True)
    bio = models.ImageField(upload_to='media/', null=True)

    def publicacao(self):
        self.data_pedido = timezone.now()
        self.save()

    def __str__(self):
        return self.produto
