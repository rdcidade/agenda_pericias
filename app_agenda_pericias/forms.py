from django.forms import ModelForm
from django import forms
from .models import tbl_pericias_agendadas, tbl_unidades, tbl_usuarios


# Atribuição de valores para os widgets do formulário
compareceu_pericia = ("Sim","Sim"),("Não","Não")
perito = ("Sim","Sim"),("Não","Não")

# Criando a classe agendar_pericias_form
class agendar_pericias_form(ModelForm):
    class Meta:
        model = tbl_pericias_agendadas
        fields=['id', 'data_pericia', 'jurisdicao','perito', 'periciado', 'cpf_parte', 'processo', 'especialidade', 'situacao_pericia', 'usuario']
        widgets = {
            'id'
            'data_pericia' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'jurisdicao' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'perito' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'periciado' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'cpf_parte' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'processo' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'especialidade' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'situacao_pericia' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'usuario' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
        }

class listar_pericias_form(ModelForm):
    class Meta:
        model = tbl_pericias_agendadas
        fields=['id', 'data_pericia', 'perito', 'periciado', 'cpf_parte', 'processo', 'especialidade', 'situacao_pericia', 'compareceu_pericia', 'hora_entrada', 'hora_saida']
        widgets = {
            'id'
            'data_pericia' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'perito' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'periciado' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'cpf_parte' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'processo' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'especialidade' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'situacao_pericia' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'compareceu_pericia' : forms.CheckboxSelectMultiple(choices= compareceu_pericia, attrs={"class":"form-check-input"}),
            'hora_entrada' : forms.TimeField (),
            'hora_saida' : forms.TimeField (),
        }

class editar_pericia_form(ModelForm):
    class Meta:
        model = tbl_pericias_agendadas
        fields = ['id', 'hora_entrada', 'hora_saida']

        widgets = {
            'id'
            'hora_entrada' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'hora_saida' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_entrada = cleaned_data.get('hora_entrada')
        hora_saida = cleaned_data.get('hora_saida')

        # Se um campo for preenchido e o outro não, exibe erro
        if (hora_entrada and not hora_saida) or (not hora_entrada and hora_saida):
            raise forms.ValidationError("Ambos os campos 'Hora Entrada' e 'Hora Saída' devem ser preenchidos.")

        return cleaned_data

class filtrar_pericias_form(ModelForm):
    class Meta:
        model = tbl_pericias_agendadas
        fields=['id', 'data_pericia', 'perito', 'periciado', 'cpf_parte', 'processo', 'especialidade', 'situacao_pericia', 'compareceu_pericia', 'hora_entrada', 'hora_saida']
        widgets = {
            'id'
            'data_pericia' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'perito' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'periciado' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'cpf_parte' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'processo' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'especialidade' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'situacao_pericia' : forms.Textarea(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
            'compareceu_pericia' : forms.CheckboxSelectMultiple(choices= compareceu_pericia, attrs={"class":"form-check-input"}),
            'hora_entrada' : forms.TimeField (),
            'hora_saida' : forms.TimeField (),
        }

class atualizar_saida_pericias_form(ModelForm):
    class Meta:
        model = tbl_pericias_agendadas
        fields=['id', 'perito', 'periciado', 'especialidade', 'compareceu_pericia', 'hora_entrada','hora_saida','usuario']
        widgets = {
            'id'
            'perito' : forms.TextInput(),
            'periciado' : forms.TextInput(),
            'especialidade' : forms.TextInput(),
            'compareceu_pericia' : forms.CheckboxInput(attrs={"class":"form-check-input"}),
            'hora_entrada' : forms.TextInput(),
            'hora_saida' : forms.TextInput(),
            'usuario' : forms.TextInput(attrs={"class":"form-control w-auto p-3 h-auto d-inline-block"}),
        }

class cadastro_usuario_form(ModelForm):
    class Meta:
        model = tbl_usuarios
        fields = ['cpf', 'usuario', 'nome', 'email', 'senha', 'unidade', 'perito']
        widgets = {
            'cpf': forms.TextInput(),
            'usuario': forms.TextInput(attrs={'type': 'hidden'}),
            'nome': forms.TextInput(),
            'email': forms.TextInput(),
            'senha': forms.PasswordInput(),
            'unidade': forms.TextInput(),
            'perito': forms.CheckboxInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        usuario = cleaned_data.get('usuario')

        # Se o campo 'usuario' vier vazio, cria automaticamente o primeiro nome
        if not usuario and nome:
            cleaned_data['usuario'] = nome.split()[0]

        return cleaned_data
        
class login_form(ModelForm):
    class Meta:
        model = tbl_usuarios
        fields=['id','cpf', 'senha', 'unidade']
        widgets = {
            'id'
            'cpf_login' : forms.Textarea(),
            'senha_login' : forms.Textarea(),
            'unidade_login' : forms.Textarea(),
        }