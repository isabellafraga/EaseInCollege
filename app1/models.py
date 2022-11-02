from django.db import models
from stdimage.models import StdImageField

class CadastroAluno(models.Model):
    CURSO_CHOICES = [
        ["Automação Industrial", "Automação Industrial"],
        ["Engenharia de Software", "Engenharia de Software"],
        ["Engenharia Elétrica", "Engenharia Elétrica"],
        ["Engenharia Mecânica", "Engenharia Mecânica"]
    ]
    PERIODO_CHOICES = [
        ["1°", "1°"], ["2°", "2°"], ["3°", "3°"], ["4°", "4°"], ["5°", "5°"],
        ["6°", "6°"], ["7°", "7°"], ["8°", "8°"], ["9°", "9°"], ["10°", "10°"]
    ]

    nomep = models.CharField(max_length=100)
    matricula = models.DecimalField(max_digits=10, decimal_places=0)
    curso = models.CharField(max_length=100, choices=CURSO_CHOICES)
    periodo = models.CharField(max_length=3, choices=PERIODO_CHOICES)
    turma = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10)
    telefone = models.CharField(max_length=14)
    CPF = models.DecimalField(max_digits=11, decimal_places=0, unique=True)


    class Meta:
        verbose_name = 'Cadastro de Aluno'
        verbose_name_plural = 'Cadastros de Alunos'

    def __str__(self):
        return self.nomep


class CadastroFuncionario(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Cadastro de Funcionário'
        verbose_name_plural = 'Cadastros de Funcionários'

    def __str__(self):
        return self.nome


class Evento(models.Model):
    CATEGORIA_CHOICES = [
        ["Curso", "Curso"],
        ["Evento Institucional", "Evento Institucional"],
        ["Evento Não Institucional", "Evento Não Institucional"],
        ["Jornada de Aprendizagem", "Jornada de Aprendizagem"],
        ["Live", "Live"],
        ["Mentoria", "Mentoria"],
        ["Palestra", "Palestra"],
    ]
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=285)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    imagem = StdImageField('imagem', upload_to='eventos', variations={'thumb': (124,124)})
    carga = models.IntegerField('carga horaria', blank=True)
    descricao = models.TextField(blank=True, default="")
    link = models.URLField()

    class Meta:
        verbose_name = 'Cadastro de Evento'
        verbose_name_plural = 'Cadastros de Eventos'

    def __str__(self):
        return self.titulo


class Emprego(models.Model):
    TIPO_CHOICES = [
        ["Estágio", "Estágio"],
        ["Registrado", "Registrado"],
    ]
    PERIODO_CHOICES = [
        ["Comercial", "Comercial"],
        ["Dia", "Dia"],
        ["Integral", "Integral"],
        ["Noite", "Noite"],
        ["12H por 16H", "12H por 16H"],
    ]
    AREA_CHOICES = [
        ["Automação", "Automação"],
        ["Elétrica", "Elétrica"],
        ["Mecânica", "Mecânica"],
        ["TI", "TI"],
    ]
    empresa = models.CharField(max_length=255, unique=True)
    site = models.URLField()
    telefone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    periodo = models.CharField(max_length=100, choices=PERIODO_CHOICES)
    area = models.CharField(max_length=100, choices=AREA_CHOICES)
    descricao = models.TextField(blank=True, default="")
    necessarios = models.TextField(default="")
    desejaveis = models.TextField(default="")
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = 'Emprego'
        verbose_name_plural = 'Empregos'

    def __str__(self):
        return self.empresa


class Sugestoes(models.Model):
    CATEGORIA_CHOICES = [
        ["AVA", "AVA"],
        ["Coordenação", "Coordenação"],
        ["Estrutura", "Estrutura"],
        ["Financeiro", "Financeiro"],
        ["Geral", "Geral"],
        ["Laboratórios", "Laboratórios"],
        ["Pedagogia", "Pedagogia"],
        ["Portal do Aluno", "Portal do Aluno"],
        ["Secretária", "Secretária"],
    ]
    assunto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES)
    anonimo = models.BooleanField()
    descricao = models.TextField(default="")

    class Meta:
        verbose_name = 'Sugestão'
        verbose_name_plural = 'Sugestões'

    def __str__(self):
        return self.assunto
