from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        # strip() = tira os espaços em Branco ou vazias 
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.WARNING, 'Preencha todos os campos')
            return render(request, 'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite duas senhas iguais')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com Sucesso')
            return render(request, 'login.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema')
            return render(request, 'cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate (username = nome,
                             password = senha)
        
        if user is not None:
            login(request, user)
            return redirect('/adotar')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha incorretos')
            return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/auth/login')