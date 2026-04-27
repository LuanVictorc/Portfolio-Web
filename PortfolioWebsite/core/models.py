from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)
    periodo = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    git = models.URLField(max_length=255, blank=True, null=True)
    linked = models.URLField(max_length=255, blank=True, null=True)
    url_imagem = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nome if self.nome else "Usuário sem nome"