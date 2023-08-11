from django.urls import path
from app.views import index, conteudo, processa_form
urlpatterns = [
    path('', index, name='index'),
    path('conteudo', conteudo, name='conteudo'),
    path('processa_form/',processa_form, name="processa_form")

]
