from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectsSerializer

# Create your views here.

class ProjectsListCreate(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    # def delete(self, request, *args, **kwargs):
    #     Projects.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = "pk"