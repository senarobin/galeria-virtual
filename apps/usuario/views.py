from django.shortcuts import render, redirect
from apps.usuario.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
            
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} Login efetuado com sucesso")
            return redirect('index')
        else:
            messages.error(request, "Erro ao efetuar o login")
            return redirect('login')
    
    return render(request, 'usuario/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
    
    if form.is_valid():    
        if form['senha_1'].value() != form['senha_2'].value():
            messages.error(request, "Você digitou senhas diferentes")
            return redirect('cadastro') 
    
        nome = form['nome_cadastro'].value()
        senha = form['senha_1'].value()
        email = form['email'].value()    
    
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Esse nome de usuário já existe")
            return redirect('cadastro')
        
        usuario = User.objects.create_user(
            username=nome,
            password=senha,
            email=email
        )
        usuario.save()
        messages.success(request, f"{nome} Cadastro realizado com sucesso")
        return redirect('login')
        
        
    return render(request, 'usuario/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')

# Create your views here.
