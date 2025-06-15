from django.shortcuts import render
from rest_framework import viewsets, serializers  # Added serializers for ValidationError
from rest_framework.permissions import IsAdminUser
from .models import Workplace, Task, Volunteer, Assignment
from .serializers import WorkplaceSerializer, TaskSerializer, VolunteerSerializer, AssignmentSerializer
from drf_spectacular.utils import extend_schema  # Import extend_schema

class WorkplaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Workplaces.

    Allows administrators to:
    - List all workplaces
    - Create a new workplace
    - Retrieve details of a specific workplace
    - Update an existing workplace
    - Delete a workplace
    """
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
    permission_classes = [IsAdminUser]
    # swagger_tags = ['Workplaces'] # drf-spectacular usually infers this well

@extend_schema(tags=['Tasks'])  # Apply tag to the whole ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Tasks.

    Tasks are associated with a Workplace. Allows administrators to:
    - List all tasks
    - Create a new task (linked to a workplace)
    - Retrieve details of a specific task
    - Update an existing task
    - Delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Volunteers'])
class VolunteerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Volunteers.

    Allows administrators to:
    - List all volunteers
    - Create a new volunteer record
    - Retrieve details of a specific volunteer
    - Update an existing volunteer's information
    - Delete a volunteer record
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Assignments'])
class AssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing Assignments of Volunteers to Tasks.

    Allows administrators to:
    - List all assignments
    - Create a new assignment (linking a Volunteer to a Task)
    - Retrieve details of a specific assignment
    - Update an existing assignment
    - Delete an assignment
    """
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAdminUser]

    @extend_schema(
        summary="Create a new assignment",
        description="Assigns a volunteer to a specific task. Ensures both volunteer and task exist before creation.",
        request=AssignmentSerializer,
        responses={201: AssignmentSerializer}
    )
    def perform_create(self, serializer):
        """
        Custom logic for creating an assignment.
        Ensures that the referenced Task and Volunteer exist.
        """
        task_id = serializer.validated_data.get('task').id
        volunteer_id = serializer.validated_data.get('volunteer').id
        try:
            Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise serializers.ValidationError({"task": "Task not found."})
        try:
            Volunteer.objects.get(id=volunteer_id)
        except Volunteer.DoesNotExist:
            raise serializers.ValidationError({"volunteer": "Volunteer not found."})
        serializer.save()
