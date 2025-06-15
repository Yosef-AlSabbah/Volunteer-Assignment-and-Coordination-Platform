from rest_framework import serializers
from .models import Workplace, Task, Volunteer, Assignment

class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

