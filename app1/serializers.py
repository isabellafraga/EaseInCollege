from rest_framework import serializers

from .models import CadastroAluno, CadastroFuncionario, Evento, Emprego, Sugestoes


class CadastroAlunoSerializer(serializers.ModelSerializer):

    class Meta:
        #extra_kargs = {
         #   'email': {'write_only': True},
          #  'senha': {'write_only': True},
           # 'telefone': {'write_only': True},
            #'CPF': {'write_only': True}
        #}
        model = CadastroAluno
        fields = (
            'nomep',
            'matricula',
            'curso',
            'periodo',
            'turma',
            'email',
            'senha',
            'telefone',
            'CPF'
        )


class CadastroFuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = CadastroFuncionario
        fields = (
            'nome',
            'departamento',
            'cargo',
            'codigo',
            'telefone',
            'email',
            'senha',
        )


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = (
            'titulo',
            'categoria',
            'data',
            'hora',
            'local',
            'rua',
            'numero',
            'imagem',
            'carga',
            'descricao',
            'link',
        )


class EmpregoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprego
        fields = (
            'empresa',
            'site',
            'telefone',
            'email',
            'tipo',
            'periodo',
            'area',
            'descricao',
            'necessarios',
            'desejaveis',
            'salario'
        )



class SugestoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sugestoes
        fields = (
            'assunto',
            'categoria',
            'anonimo',
            'descricao',
        )