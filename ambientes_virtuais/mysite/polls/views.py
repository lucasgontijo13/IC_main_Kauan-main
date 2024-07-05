#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Cliente

def registro_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário se forem válidos
            form.save()
            return redirect('sucesso')
    else:
        form = LoginForm()

    return render(request, 'registro.html', {'form': form})



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

def login(request):
    return render(request, 'login.html')

def password(request):
    return render(request, 'password.html')

def register(request):
    return render(request, 'register.html')

def tables(request):
    return render(request, 'tables.html')



"""
def usuario(request):
    #salvar os dados da tela para o banco de dados
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    #novo_cliente. = request.POST.get('sobrenome')
    novo_cliente.cpf = request.POST.get('cpf')
    novo_cliente.cnpj = request.POST.get('cnpj')
    novo_cliente.email = request.POST.get('email')
    #novo_cliente.s = request.POST.get('senha')
    novo_cliente.save()
    cliente = {
        'cliente' : Cliente.objects.all()
    }
    return render(request,'templates/clientes.html')
"""