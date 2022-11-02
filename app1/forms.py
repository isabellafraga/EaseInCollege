from django import forms
from app1.models import CadastroAluno, CadastroFuncionario, Evento, Emprego, Sugestoes


class FormFuncionario(forms.ModelForm):
    class Meta:
        model = CadastroFuncionario
        fields = '__all__'

    def __str__(self):
        return self.nome


class FormAluno(forms.ModelForm):
    class Meta:
        model = CadastroAluno
        fields = '__all__'

    def __str__(self):
        return self.nomep


class FormEvento(forms.ModelForm):
    data = forms.DateField(label='Data', localize=True, required=True,
                           widget=forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}))

    class Meta:
        model = Evento
        fields = '__all__'

    def __str__(self):
        return self.titulo


class FormEmprego(forms.ModelForm):
    class Meta:
        model = Emprego
        fields = '__all__'

    def __str__(self):
        return self.empresa


class FormSugestao(forms.ModelForm):
    class Meta:
        model = Sugestoes
        fields = '__all__'

    def __str__(self):
        return self.assunto