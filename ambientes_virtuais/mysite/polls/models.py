from django.db import models
from django.utils import timezone  # Adicione esta linha

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cnpj = models.CharField(max_length=14, default='00000000000000')
    data_criacao = models.DateTimeField(default=timezone.now)  # Adicionar valor padrão
    data_atualizacao = models.DateTimeField(auto_now=True)  # Adicionar data e hora de atualização

    def __str__(self):
        return self.nome

class Login(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relacionamento com Cliente
    email = models.EmailField(max_length=50, unique=True, null=False, default='default@example.com')
    senha = models.CharField(max_length=8, null=True)  # Limitar senha para 8 caracteres

    def __str__(self):
        return self.email