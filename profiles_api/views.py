from rest_framework.views import  APIView
from rest_framework.response import Response

#import from serializer
from rest_framework import status
from profiles_api import  serializer

# Create your views here.

class HelloAPIView(APIView):
    """ API View of Hello world"""

    serializer_class = serializer.HelloSerializers

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

    def post(self, request):
        """ Create a message with our name"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            # 'name' is the attribute defined in profiles_api/serializer.py
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return  Response({'message': message})
        else:
            #
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Update a object
            In this case we dont use ID (PK)
        """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

