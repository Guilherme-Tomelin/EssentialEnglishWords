from django.urls import path
from app.views import index, conteudo

urlpatterns = [
    path('', index, name='index'),
    path('conteudo', conteudo, name='conteudo'),

]
