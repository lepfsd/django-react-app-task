from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_slug, convert_lower

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        
        queryset = Task.objects.all()
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author=author)
        completed = self.request.query_params.get('completed', None)
        if completed is not None:
            queryset = queryset.filter(completed=completed)
        return queryset
    

    @action(detail=False, methods=['post'], url_path='task-slug')
    def task_slug(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'text is required'}, status=status.HTTP_400_BAD_REQUEST)
        slug = generate_slug(text)
        return Response({'slug': slug}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'], url_path='task-lower')
    def task_lower(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'text is required'}, status=status.HTTP_400_BAD_REQUEST)
        lower = convert_lower(text) 
        return Response({'text': lower}, status=status.HTTP_200_OK)