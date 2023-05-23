from rest_framework import serializers
from .models import ToDo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = ['uuid', 'todo_title', 'todo_description']