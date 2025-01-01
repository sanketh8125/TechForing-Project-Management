from rest_framework.viewsets import ModelViewSet
from .models import Users, Projects, ProjectMembers, Tasks, Comments
from .serializers import UserRegistrationSerializer, UserSerializer, ProjectSerializer, ProjectMemberSerializer, TaskSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserRegistrationViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer
    http_method_names = ['post']

class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectMemberViewSet(ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = ProjectMemberSerializer

class TaskListViewCreate(APIView):
    def get(self, request, project_id):
        tasks = Tasks.objects.filter(project_id=project_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, project_id):
        try:
            project = Projects.objects.get(id=project_id)
        except Projects.DoesNotExist:
            raise NotFound("Project not found")

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(project=project)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskCommentsViewCreate(APIView):
    def get(self, request, task_id):
        try:
            task = Tasks.objects.get(pk=task_id)
        except Tasks.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        comments = Comments.objects.filter(task=task)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, task_id):
        try:
            task = Tasks.objects.get(pk=task_id)
        except Tasks.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task=task) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
