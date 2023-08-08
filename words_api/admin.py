from django.contrib import admin
from words_api.models import Palavra

class Palavras(admin.ModelAdmin):
    list_display = ('id','word','pronunciation','translation')
    list_display_links = ('id', 'word')
    search_fields = ('id', 'word',)
    list_per_page = 50

admin.site.register(Palavra,Palavras)
    