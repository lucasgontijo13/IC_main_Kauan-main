from django.shortcuts import render, redirect
from .forms import ClienteForm


def registro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso após o registro
    else:
        form = ClienteForm()
    
    return render(request, 'register.html', {'form': form})

def sucesso_view(request):
    return render(request, 'index.html')


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



