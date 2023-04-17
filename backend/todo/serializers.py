"""
Serializers for the Todo model which convert Todo objects to JSON format for use in API responses.
"""
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Todo model to convert Todo objects to JSON format. 
    """
    class Meta:
        """
        Meta class to specify the Todo model and fields to include in the serialized output.
        """
        model = Todo
        fields = ('id', 'title', 'description', 'completed','due_date','priority')
    def validate(self, attrs):
        if len(attrs['title']) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long.')
        return attrs
