from django.shortcuts import render
from core.models import Usuario
from .models import Certificado, Projeto

def home(request):
    # Pegamos o primeiro (e único) usuário do banco
    perfil = Usuario.objects.first()
    # Pegamos todos os certificados cadastrados
    certificados = Certificado.objects.all()
    
    context = {
        'usuario': perfil,
        'certificados': certificados
    }
    return render(request, 'portfolio/home.html', context)


def projetos(request):
    lista_projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': lista_projetos})