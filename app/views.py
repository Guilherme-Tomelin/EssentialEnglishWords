from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from words_api.models import Palavra
from django.http import HttpResponse
import random



def index(request):
    return render(request, 'app/index.html')

@login_required(login_url='login') 
def conteudo(request):
      
    word_count = Palavra.objects.count()

    random_number = random.randint(0, word_count -1)

    random_word = Palavra.objects.all()[random_number]

    print(f'A palavra aleatória é: {random_word}')

    return render(request, 'app/conteudo.html', {'palavra_aleatoria': random_word, 'user': request.user})


def processa_form(request):
    translationInput = request.POST.get('translationInput')
    sentenceInput = request.POST.get('sentenceInput')

    print(f'Tradução [{translationInput}] Frase [{sentenceInput}]')

    resultado = processa_palavra(translationInput)

    if resultado['']:
        pass
    #return HttpResponse(f'Tradução [{translationInput}] Frase [{sentenceInput}]')

def configuracoes(request):
    return render(request,'app/configuracoes.html')



def processa_palavra(translationInput):
    print(f'Função processa_palavra {translationInput}')

    try:
        palavra_obj = Palavra.objects.get(word=translationInput)
        translation = palavra_obj.translation

        return {
            'palavra_encontrada': True,
            'translation': translation,
        }

    except Palavra.DoesNotExist:
        return {'palavra_encontrada': False}
    


















