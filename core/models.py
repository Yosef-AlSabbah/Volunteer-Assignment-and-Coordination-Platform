from django.db import models

# Create your models here.

class Workplace(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    workplace = models.ForeignKey(Workplace, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} at {self.workplace.name}"

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255) # Can be email or phone

    def __str__(self):
        return self.name

class Assignment(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # Workplace is implicitly defined via Task's workplace
    # If a task can be independent of a workplace, or an assignment can be to a workplace directly,
    # then a direct ForeignKey to Workplace would be needed here.
    # For now, assuming task is always tied to a workplace.
    date_assigned = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.volunteer.name} assigned to {self.task.name} at {self.task.workplace.name}"
