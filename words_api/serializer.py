from rest_framework import serializers
from words_api.models import Palavra



class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavra
        fields = '__all__'