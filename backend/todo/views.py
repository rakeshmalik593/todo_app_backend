"""
This module defines views for the Todo app.

The TodoView class is a viewset for the Todo model, which provides CRUD operations
(Create, Retrieve, Update, Delete) for Todo objects. This viewset uses the TodoSerializer
to convert Todo objects to JSON format for use in API responses.
"""
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    """
    A viewset for the Todo model which provides CRUD operations for Todo objects.

    This viewset uses the TodoSerializer to convert Todo objects to JSON format.
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    