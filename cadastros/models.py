from django.db import models

# Create your models here.

class Pessoas(models.Model):
    estado_civil = [
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('U', 'Uniao estável'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viuvo(a)')
    ]

    codigo = models.CharField(max_length=5, primary_key=True)
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=10, null=True, blank=True)
    expedidor= models.CharField(max_length=12, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    titulo = models.CharField(max_length=12, null=True, blank=True)
    nacionalidade= models.CharField(max_length=15, null=True, blank=True)
    natural= models.CharField(max_length=30, null=True, blank=True)
    estado_civil= models.CharField(max_length=1,null= True, choices=estado_civil)
    qtd_dependentes=models.DecimalField(max_digits=5, decimal_places=2)
    rua = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=4, null=True, blank=True)
    complemento = models.CharField(max_length=20, null=True, blank=True)
    bairro = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    cidade = models.CharField(max_length=30, null=True, blank=True)
    estado= models.CharField(max_length=2, null=True, blank=True)
    celular1= models.CharField(max_length=15, null=True, blank=True)
    celular2= models.CharField(max_length=15, null=True, blank=True)
    e_mail=models.EmailField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.nome



