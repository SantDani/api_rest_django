from rest_framework import  serializers

class HelloSerializers(serializers.Serializer):
    """ Serializers one input for test ouw APIview """
    name = serializers.CharField(max_length=10)
