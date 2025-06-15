from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkplaceViewSet, TaskViewSet, VolunteerViewSet, AssignmentViewSet

router = DefaultRouter()
router.register(r'workplaces', WorkplaceViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

