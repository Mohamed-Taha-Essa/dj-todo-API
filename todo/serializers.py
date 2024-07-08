from rest_framework import serializers
from . models import ToDo


class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields= '__all__'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'