from django.contrib import admin

# Register your models here.
from .models import Certificado, Projeto

admin.site.register(Certificado)
admin.site.register(Projeto)