from django.urls import path
from . import views

urlpatterns = [
    path('projectposts/', views.ProjectsListCreate.as_view(), name='projects-view-create'),
    path('projectposts/<int:pk>/', views.ProjectsRetrieveUpdateDestroy.as_view(), name='projects-retrieveUpdateDestroy'),
]