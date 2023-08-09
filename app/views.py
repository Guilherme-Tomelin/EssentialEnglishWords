from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'app/index.html')

def conteudo(request):
    if not request.user.is_authenticated:
        return redirect('/login')    
        
    return render(request, 'app/conteudo.html')


