from django.db import models

# Create your models here.
class Produtos(models.Model):
    status_produto = [
        ('D', 'disponível'),
        ('I', 'indisponivel')
    ]
    codproduto = models.AutoField( primary_key=True, verbose_name="codigo do produto")
    descproduto = models.CharField(max_length=150, verbose_name="produto")
    marca = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    unidade= models.CharField(max_length=20)
    fornecedor = models.CharField(max_length=100)
    preco = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to= 'media', blank=True, null = True)
    situacao = models.CharField(max_length=20, null=True, choices=status_produto)

    def __str__(self):
        return  self.descproduto
