from django.shortcuts import render, redirect
from users.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["password"].value() != form["password2"].value():
                messages.error(request, "As senhas não correspondem.")
                return redirect('cadastro')
            
            name=form["user_name_c"].value()
            email=form["email"].value()
            password=form["password"].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, "Usuário(a) já existente.")
                return redirect('login')

            usuario = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            usuario.save()
            messages.error(request, "Cadastro realizado com sucesso!")
            return redirect('login')



    return render(request, 'app/cadastro.html', {"form": form})

def login(request):
    form = LoginForms

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name=form['user_name_l'].value()
            password=form['password'].value()

        user = auth.authenticate(
            request,
            username=name,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request,f"Olá {name}, Você está logado!")
            return redirect('conteudo')
        else:
            messages.error(request, "Erro ao efetuar login.")
            return redirect('login')

    return render(request, 'app/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request,"logout efetuado com sucesso!")

    return redirect('login')