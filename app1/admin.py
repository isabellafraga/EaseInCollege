from django.contrib import admin

from .models import CadastroAluno, CadastroFuncionario, Evento, Emprego, Sugestoes

@admin.register(CadastroAluno)
class CadastroAlunoAdmin(admin.ModelAdmin):
    list_display = ('nomep', 'matricula', 'curso', 'periodo', 'turma', 'email', 'senha', 'telefone', 'CPF')


@admin.register(CadastroFuncionario)
class CadastroFuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'departamento', 'cargo', 'codigo', 'telefone', 'email', 'senha')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data', 'hora', 'local', 'rua', 'numero', 'carga', 'descricao', 'link')


@admin.register(Emprego)
class EmpregoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'site', 'telefone', 'email', 'tipo', 'periodo', 'area', 'descricao', 'necessarios', 'desejaveis', 'salario')


@admin.register(Sugestoes)
class SugestoesAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'categoria', 'anonimo', 'descricao')


