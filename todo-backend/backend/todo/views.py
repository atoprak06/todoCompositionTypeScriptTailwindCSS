from rest_framework import viewsets
from rest_framework import response
from .serializers import TodoSerializer
from rest_framework import permissions
from .models import Todo

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

 
