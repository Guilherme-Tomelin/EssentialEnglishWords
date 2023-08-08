from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def conteudo(request):
    return render(request, 'app/conteudo.html')


