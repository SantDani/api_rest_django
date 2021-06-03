from rest_framework.views import  APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """ API View of Hello world"""

    def get(self, request, format=None):
        """ Return list of characteristics """

        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los URLs',
        ]

        # Need a list o dictionary for transform to JSON
        return Response({'message': 'Hello', 'an_appview': an_apiview})