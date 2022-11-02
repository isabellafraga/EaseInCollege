from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CadastroAluno
from .serializers import CadastroAlunoSerializer

class CadastroAlunoAPIView(APIView):
    """
    API de Cadastros de Alunos
    """
    def get(self, request):
        cadastroAluno = CadastroAluno.objects.all()
        serilizer = CadastroAlunoSerializer(cadastroAluno, many=True)
        return Response(serilizer.data)

    def post(self, request):
        serializer = CadastroAlunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)