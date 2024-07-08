from rest_framework import viewsets
from . serializers import ToDoSerializers
from . models import ToDo  


class ToDoViewSets(viewsets.ModelViewSet):
    serializer_class = ToDoSerializers
    queryset = ToDo.objects.all()

    xxx