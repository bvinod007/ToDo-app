from rest_framework import serializers
from .models import ToDo, TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = ToDo
        fields = ['uuid', 'todo_title', 'slug','todo_description', 'is_done']

    def get_slug(self, obj):
        return slugify(obj.todo_title)
    
    def validate_todo_title(self, validated_data):
        if validated_data:
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if not regex.search(validated_data) == None:
                raise serializers.ValidationError('Todo title can not contain special characters')
            if len(validated_data) < 3:
                raise serializers.ValidationError('Todo title length can not be less than 3 chars')
            
        return validated_data

    # def validate(self, validated_data):
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError('Todo title can not contain special characters')
            
        # return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        # exclude = ['created_at', 'updated_at']
        fields = '__all__'
        # depth = 1