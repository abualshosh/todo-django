from .models import Task, Context, List
from rest_framework import serializers

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"
class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        list = ListSerializer(required=True)
        context = ContextSerializer(read_only=True)
        fields = "__all__"
        # depth = 1
     
    #  def create(self, validated_data):
    # #     return List.objects.create(**validated_data)
    #     context = Context.objects.create(**validated_data)
    #     return Task.objects.create(context=constext, **validated_data)
    #     return context

    # def update(self, instance, validated_data):
    #     instance.__dict__.update(**validated_data)
    #     instance.save()

    #     return instance
