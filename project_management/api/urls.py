from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, TaskCommentsViewCreate, CommentViewSet, UserRegistrationViewSet,LoginView

router = DefaultRouter()
router.register('users/register', UserRegistrationViewSet, basename='user-registration')
router.register('users', UserViewSet, basename='user')
router.register('projects', ProjectViewSet)
router.register('projectMembers', ProjectMemberViewSet)
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)
urlpatterns = [
    path('users/login/', LoginView.as_view(), name='user_login'),
    path('projects/<int:project_id>/tasks/', views.TaskListViewCreate.as_view(), name='task-list'),
    path('tasks/<int:task_id>/comments/', TaskCommentsViewCreate.as_view(), name='task-comments'),
  ] + router.urls