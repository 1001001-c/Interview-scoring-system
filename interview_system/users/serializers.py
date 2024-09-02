from rest_framework import serializers

from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    examiners_file = serializers.FileField()
    candidates_file = serializers.FileField()