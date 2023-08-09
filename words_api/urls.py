from django.urls import path, include
from rest_framework import routers
from words_api.views import PalavrasViewSet

router = routers.DefaultRouter()
router.register('words', PalavrasViewSet, basename='Words')

urlpatterns = [
    path('api',include(router.urls)),
    #path('upload-json/', JSONUploadView.as_view(), name='json-upload'),
]
