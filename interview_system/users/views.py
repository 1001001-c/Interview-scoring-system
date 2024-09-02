# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from .services import process_csv_files

class FileUploadView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            examiners_file = request.FILES.get('examiners_file')
            candidates_file = request.FILES.get('candidates_file')
            process_csv_files(examiners_file, candidates_file)
            return Response({'status': 'Files processed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)