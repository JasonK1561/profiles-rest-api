from rest_framework import serializers
#It's good practice to have a serializer file in each app if needed
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    """Takes in a name input and then add it to our APIView and use it to test
    our POST functionality in our APIView"""
    """Serializers also do validation for fields"""
    name = serializers.CharField(max_length=10)
