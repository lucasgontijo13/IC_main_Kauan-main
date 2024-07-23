import logging
from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login as auth_login

from .models import Cliente, Login
from django.contrib.auth.hashers import check_password

logger = logging.getLogger('django')

def registro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                logger.info('Cliente salvo com sucesso!')
                return redirect('index')  # Redireciona para a página de sucesso após o registro
            except IntegrityError:
                # As mensagens de erro já foram adicionadas ao formulário no método save()
                pass
        else:
            logger.error('Formulário inválido: %s', form.errors)
    else:
        form = ClienteForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar se o cliente existe com o email fornecido
        try:
            cliente = Cliente.objects.get(email=email)
            if check_password(password, cliente.senha):  # Verifica se a senha está correta
                # Autenticação bem-sucedida
                request.session['cliente_id'] = cliente.id
                
                # Registrar o login
                Login.objects.create(
                    cliente=cliente,
                    descricao='Realizou Login'
                )
                
                return redirect('index')  # Redirecionar para a página inicial ou outra página após o login
            else:
                messages.error(request, 'Email ou senha incorretos')
        except Cliente.DoesNotExist:
            messages.error(request, 'Email ou senha incorretos')
    
    return render(request, 'login.html')



def index(request):
    return render(request, 'index.html')

def error_401(request):
    return render(request, '401.html')

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')

def charts(request):
    return render(request, 'charts.html')

def layout_sidenav_light(request):
    return render(request, 'layout-sidenav-light.html')

def layout_static(request):
    return render(request, 'layout-static.html')

def password(request):
    return render(request, 'password.html')

def register(request):
    return render(request, 'register.html')

def tables(request):
    return render(request, 'tables.html')



