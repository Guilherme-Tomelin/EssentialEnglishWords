from rest_framework import viewsets
from words_api.models import Palavra
from words_api.serializer import WordSerializer

class PalavrasViewSet(viewsets.ModelViewSet):
    """Exibe todas as palavras"""

    queryset = Palavra.objects.all()
    serializer_class = WordSerializer




# views.py
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Palavra
# from .serializer import WordSerializer

# class JSONUploadView(APIView):
#     parser_classes = [JSONParser]

#     def post(self, request, format=None):
#         data = request.data.get('data', [])  # Obtém a lista de palavras do JSON
#         serializer = WordSerializer(data=data, many=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
