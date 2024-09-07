
# Create your views here.
# exams/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Exam
from .serializers import ExamSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
