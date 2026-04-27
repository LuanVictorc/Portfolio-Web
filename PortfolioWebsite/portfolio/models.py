from django.db import models

# Create your models here.

class Certificado(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.descricao if self.descricao else "Certificado sem descrição"

class Projeto(models.Model):
    TIPO_CHOICES = [
        ('PESSOAL', 'Pessoal'),
        ('DISCIPLINA', 'Disciplina'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='PESSOAL', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    link_git = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nome if self.nome else "Projeto sem nome"