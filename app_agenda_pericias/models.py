from django.db import models
from django.contrib.auth.hashers import make_password

class tbl_pericias_agendadas(models.Model):
    data_pericia = models.CharField(max_length=20, blank=True, null=True)
    jurisdicao = models.CharField(max_length=100, blank=True, null=True)
    perito = models.CharField(max_length=100, blank=True, null=True)
    periciado = models.CharField(max_length=100, blank=True, null=True)
    cpf_parte = models.CharField(max_length=14, blank=True, null=True)
    processo = models.CharField(max_length=100, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    situacao_pericia = models.CharField(max_length=100, blank=True, null=True)
    compareceu_pericia = models.BooleanField(default=False)
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()
    usuario = models.CharField(max_length=50, blank=True, null=True)
    data_marcada = models.DateField(blank=True, null=True)
    hora_marcada = models.TimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'tbl_pericias_agendadas'
        unique_together = ('periciado', 'processo', 'data_pericia', 'situacao_pericia')
        indexes = [
            models.Index(fields=['periciado', 'processo', 'data_pericia', 'situacao_pericia']),
        ]

    def __str__(self):
        return f'{self.periciado} - {self.processo} - {self.data_pericia} - {self.situacao_pericia}'

class tbl_usuarios(models.Model):
    cpf = models.CharField(max_length=11, blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=128)  # aumenta o tamanho por segurança
    unidade = models.CharField(max_length=3, blank=True, null=True)
    perito = models.BooleanField(blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'tbl_usuarios'

    def save(self, *args, **kwargs):
        # Criptografa a senha apenas se ela ainda não estiver criptografada
        if not self.senha.startswith('pbkdf2_'):
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class tbl_unidades(models.Model):
    subsecao = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_unidades'

    def __str__(self):
        return self.subsecao
    
class tbl_salas(models.Model):
    sala = models.CharField(max_length=25, blank=True, null=True)
    perito = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'tbl_salas'

class tbl_peritos(models.Model):
    cpf = models.CharField(max_length=11, blank=True, null=True)
    nome_perito = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'tbl_peritos'
