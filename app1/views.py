from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from rest_framework import generics

from .forms import FormFuncionario, FormAluno, FormEvento, FormEmprego, FormSugestao
from .models import CadastroAluno, CadastroFuncionario, Evento, Emprego, Sugestoes
from .serializers import CadastroAlunoSerializer, CadastroFuncionarioSerializer, \
    EventoSerializer, EmpregoSerializer, SugestoesSerializer


def imagem_eventos(request):
    context = {'noticias': Evento.objects.all()}
    return render(request, "app3/evento/lista.html", context)

# PÁGINA PRINCIPAL INDEX
# ----------------------------------------------
def indexx(request):
    return render(request, 'app3/index.html')

# PÁGINA PRINCIPAL LOGIN
# ----------------------------------------------
def loginn(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app1:indexx'))
            else:
                return HttpResponse("Sua Conta Não Esta Ativa.")
        else:
            print("Alguém Tentou Fazer Login e Falhou")
            print("Foi Usado userName: {} e senha: {}".format(usuario, senha))
            return HttpResponse("O Login ou Senha Está Incorreto.")

    else:
        return render(request, 'app3/login.html', {})


# PÁGINA PRINCIPAL LOGOUT
# ----------------------------------------------
@login_required
def logoutt(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


# PÁGINA CADASTRO FUNCIONARIO
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "app3/funcionario/cadastra.html"
    model = CadastroFuncionario
    form_class = FormFuncionario
    success_url = reverse_lazy("app1:lista_funcionarios")


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "app3/funcionario/lista.html"
    model = CadastroFuncionario
    context_object_name = "funcionarios"


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "app3/funcionario/atualiza.html"
    model = CadastroFuncionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("app1:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "app3/funcionario/exclui.html"
    model = CadastroFuncionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("app1:lista_funcionarios")


##################################################################################


# PÁGINA CADASTRO ALUNO
# ----------------------------------------------

class AlunoCreateView(CreateView):
    template_name = "app3/aluno/cadastra.html"
    model = CadastroAluno
    form_class = FormAluno
    success_url = reverse_lazy("app1:lista_alunos")


# LISTA DE ALUNO
# ----------------------------------------------

class AlunoListView(ListView):
    template_name = "app3/aluno/lista.html"
    model = CadastroAluno
    context_object_name = "alunos"


# ATUALIZAÇÃO DE ALUNO
# ----------------------------------------------

class AlunoUpdateView(UpdateView):
    template_name = "app3/aluno/atualiza.html"
    model = CadastroAluno
    fields = '__all__'
    context_object_name = 'aluno'
    success_url = reverse_lazy("app1:lista_alunos")


# EXCLUSÃO DE ALUNO
# ----------------------------------------------

class AlunoDeleteView(DeleteView):
    template_name = "app3/aluno/exclui.html"
    model = CadastroAluno
    context_object_name = 'aluno'
    success_url = reverse_lazy("app1:lista_alunos")


##################################################################################


# PÁGINA CADASTRO EVENTO
# ----------------------------------------------

class EventoCreateView(CreateView):
    template_name = "app3/evento/cadastra.html"
    model = Evento
    form_class = FormEvento
    success_message = 'Cadastro realizado com sucesso'
    success_url = reverse_lazy("app1:lista_eventos")


# LISTA DE EVENTO
# ----------------------------------------------

class EventoListView(ListView):
    template_name = "app3/evento/lista.html"
    model = Evento
    context_object_name = "eventos"


# ATUALIZAÇÃO DE EVENTO
# ----------------------------------------------

class EventoUpdateView(UpdateView):
    template_name = "app3/evento/atualiza.html"
    model = Evento
    fields = '__all__'
    context_object_name = 'evento'
    success_url = reverse_lazy("app1:lista_eventos")


# EXCLUSÃO DE ALUNO
# ----------------------------------------------

class EventoDeleteView(DeleteView):
    template_name = "app3/evento/exclui.html"
    model = Evento
    context_object_name = 'evento'
    success_url = reverse_lazy("app1:lista_eventos")


##################################################################################

# PÁGINA CADASTRO EMPREGO
# ----------------------------------------------

class EmpregoCreateView(CreateView):
    template_name = "app3/emprego/cadastra.html"
    model = Emprego
    form_class = FormEmprego
    success_message = 'Cadastro realizado com sucesso'
    success_url = reverse_lazy("app1:lista_empregos")


# LISTA DE EMPREGO
# ----------------------------------------------

class EmpregoListView(ListView):
    template_name = "app3/emprego/lista.html"
    model = Emprego
    context_object_name = "empregos"


# ATUALIZAÇÃO DE EMPREGO
# ----------------------------------------------

class EmpregoUpdateView(UpdateView):
    template_name = "app3/emprego/atualiza.html"
    model = Emprego
    fields = '__all__'
    context_object_name = 'emprego'
    success_url = reverse_lazy("app1:lista_empregos")


# EXCLUSÃO DE EMPREGO
# ----------------------------------------------

class EmpregoDeleteView(DeleteView):
    template_name = "app3/emprego/exclui.html"
    model = Emprego
    context_object_name = 'emprego'
    success_url = reverse_lazy("app1:lista_empregos")


##################################################################################

# PÁGINA CADASTRO SUGESTÃO
# ----------------------------------------------

class SugestaoCreateView(CreateView):
    template_name = "app3/sugestao/cadastra.html"
    model = Sugestoes
    form_class = FormSugestao
    success_message = 'Cadastro realizado com sucesso'
    success_url = reverse_lazy("app1:lista_sugestoes")


# LISTA DE SUGESTÃO
# ----------------------------------------------

class SugestaoListView(ListView):
    template_name = "app3/sugestao/lista.html"
    model = Sugestoes
    context_object_name = "sugestoes"


# ATUALIZAÇÃO DE SUGESTÃO
# ----------------------------------------------

class SugestaoUpdateView(UpdateView):
    template_name = "app3/sugestao/atualiza.html"
    model = Sugestoes
    fields = '__all__'
    context_object_name = 'sugestao'
    success_url = reverse_lazy("app1:lista_sugestoes")


# EXCLUSÃO DE SUGESTÃO
# ----------------------------------------------

class SugestaoDeleteView(DeleteView):
    template_name = "app3/sugestao/exclui.html"
    model = Sugestoes
    context_object_name = 'sugestao'
    success_url = reverse_lazy("app1:lista_sugestoes")


##################################################################################

#----API ALUNO----#
#Lista e Criar
class CadastrosAlunosAPIView(generics.ListCreateAPIView):
    queryset = CadastroAluno.objects.all()
    serializer_class = CadastroAlunoSerializer

#Trazer por id, atualizar por id, deletar por id
class CadastroAlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CadastroAluno.objects.all()
    serializer_class = CadastroAlunoSerializer
#----API ALUNO----#

#----API FUNCIONARIO----#
#Lista e Criar
class CadastrosFuncionariosAPIView(generics.ListCreateAPIView):
    queryset = CadastroFuncionario.objects.all()
    serializer_class = CadastroFuncionarioSerializer

#Trazer por id, atualizar por id, deletar por id
class CadastroFuncionarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CadastroFuncionario.objects.all()
    serializer_class = CadastroFuncionarioSerializer
#----API FUNCIONARIO----#

#----API EVENTO----#
#Lista e Criar
class EventosAPIView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

#Trazer por id, atualizar por id, deletar por id
class EventoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
#----API EVENTO----#

#----API EMPREGO----#
#Lista e Criar
class EmpregosAPIView(generics.ListCreateAPIView):
    queryset = Emprego.objects.all()
    serializer_class = EmpregoSerializer

#Trazer por id, atualizar por id, deletar por id
class EmpregoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprego.objects.all()
    serializer_class = EmpregoSerializer
#----API EMPREGO----#

#----API SUGESTAO----#
#Lista e Criar
class SugestoesAPIView(generics.ListCreateAPIView):
    queryset = Sugestoes.objects.all()
    serializer_class = SugestoesSerializer

#Trazer por id, atualizar por id, deletar por id
class SugestaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sugestoes.objects.all()
    serializer_class = SugestoesSerializer
#----API SUGESTAO----#