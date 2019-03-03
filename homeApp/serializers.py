from rest_framework.serializers import ModelSerializer
from .models import Task, AddTask, Code


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'task_name',
            'task_start_time',
            'task_end_time'
        )

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.task_start_time = validated_data.get('task_start_time', instance.task_start_time)
        instance.task_end_time = validated_data.get('task_end_time', instance.task_end_time)
        return instance


class AddTaskSerializer(ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = AddTask
        fields = (
            'id',
            'category',
            'tasks'
        )
    #
    # def create(self, validated_data):
    #     tasks_data = validated_data.pop('tasks')
    #     _tasks = AddTask.objects.create(**validated_data)
    #     for _task in tasks_data:
    #         Task.objects.create(_tasks=_tasks, **_task)
    #     return _tasks


class CodeSerializer(ModelSerializer):
    class Meta:
        model = Code
        fields = (
            'id',
            'code',
            'created_date'
        )

    def create(self, validated_data):
        return Code.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        return instance
