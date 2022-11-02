from django.conf.urls.static import static
from django.urls import path

from EaseInCollege import settings
from . import views

from .views import CadastroAlunoAPIView, CadastrosAlunosAPIView, CadastroFuncionarioAPIView, \
    CadastrosFuncionariosAPIView, EventoAPIView, EventosAPIView, EmpregoAPIView, EmpregosAPIView, \
    SugestaoAPIView, SugestoesAPIView, FuncionarioListView, FuncionarioUpdateView, \
    FuncionarioDeleteView, FuncionarioCreateView, AlunoCreateView, AlunoListView, AlunoUpdateView, \
    AlunoDeleteView, EventoCreateView, EventoListView, EventoUpdateView, EventoDeleteView, EmpregoCreateView, \
    EmpregoListView, EmpregoUpdateView, EmpregoDeleteView, SugestaoCreateView, SugestaoListView, SugestaoUpdateView, \
    SugestaoDeleteView

app_name = "app1"

urlpatterns = [
    path('', views.imagem_eventos, name="listar_eventos"),
    path('login', views.loginn, name='login'),
    path('logout', views.logoutt, name='logout'),
    path('indexx', views.indexx, name='indexx'),

######################################################################################################

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),

######################################################################################################

    # GET /aluno/cadastrar
    path('aluno/cadastrar', AlunoCreateView.as_view(), name="cadastra_aluno"),

    # GET /alunos
    path('alunos/', AlunoListView.as_view(), name="lista_alunos"),

    # GET/POST /aluno/{pk}
    path('aluno/<pk>', AlunoUpdateView.as_view(), name="atualiza_aluno"),

    # GET/POST /alunos/excluir/{pk}
    path('aluno/excluir/<pk>', AlunoDeleteView.as_view(), name="deleta_aluno"),

######################################################################################################

    # GET /evento/cadastrar
    path('evento/cadastrar', EventoCreateView.as_view(), name="cadastra_evento"),

    # GET /eventos
    path('eventos/', EventoListView.as_view(), name="lista_eventos"),

    # GET/POST /evento/{pk}
    path('evento/<pk>', EventoUpdateView.as_view(), name="atualiza_evento"),

    # GET/POST /eventos/excluir/{pk}
    path('evento/excluir/<pk>', EventoDeleteView.as_view(), name="deleta_evento"),

######################################################################################################

    # GET /emprego/cadastrar
    path('emprego/cadastrar', EmpregoCreateView.as_view(), name="cadastra_emprego"),

    # GET /empregos
    path('empregos/', EmpregoListView.as_view(), name="lista_empregos"),

    # GET/POST /emprego/{pk}
    path('emprego/<pk>', EmpregoUpdateView.as_view(), name="atualiza_emprego"),

    # GET/POST /emprego/excluir/{pk}
    path('emprego/excluir/<pk>', EmpregoDeleteView.as_view(), name="deleta_emprego"),

######################################################################################################

    # GET /sugestao/cadastrar
    path('sugestao/cadastrar', SugestaoCreateView.as_view(), name="cadastra_sugestao"),

    # GET /sugestoes
    path('sugestoes/', SugestaoListView.as_view(), name="lista_sugestoes"),

    # GET/POST /sugestao/{pk}
    path('sugestao/<pk>', SugestaoUpdateView.as_view(), name="atualiza_sugestao"),

    # GET/POST /sugestao/excluir/{pk}
    path('sugestao/excluir/<pk>', SugestaoDeleteView.as_view(), name="deleta_sugestao"),

    # API ---------------------- ###################################################################

    path('APIcadastro_aluno/', CadastrosAlunosAPIView.as_view(), name='cadastros_alunos'),
    path('APIcadastro_aluno/<int:pk>/', CadastroAlunoAPIView.as_view(), name='cadastro_aluno'),

    path('APIcadastro_funcionario/', CadastrosFuncionariosAPIView.as_view(), name='cadastros_funcionarios'),
    path('APIcadastro_funcionario/<int:pk>/', CadastroFuncionarioAPIView.as_view(), name='cadastro_funcionario'),

    path('APIevento/', EventosAPIView.as_view(), name='eventos'),
    path('APIevento/<int:pk>/', EventoAPIView.as_view(), name='evento'),

    path('APIemprego/', EmpregosAPIView.as_view(), name='empregos'),
    path('APIemprego/<int:pk>/', EmpregoAPIView.as_view(), name='emprego'),

    path('APIsugestao/', SugestoesAPIView.as_view(), name='sugestoes'),
    path('APIsugestao/<int:pk>/', SugestaoAPIView.as_view(), name='sugestao'),
]