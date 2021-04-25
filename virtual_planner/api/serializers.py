from rest_framework import serializers
from .models import Goal, Work

#Creates serialzers to turn Py object into json. Reference model and fields to show

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'text', 'due_date', 'goal_type', 'completed')

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'text', 'due_date', 'work_type', 'completed')


class PostGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('text', 'due_date', 'goal_type')

class PostWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('text', 'due_date', 'work_type')