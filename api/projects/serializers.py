from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["id", "name", "description", "companies", "content", "duration", "imageUrl"]