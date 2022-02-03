from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blog
from project.models import Project
from project.serializers import ProjectSerializer
from blog.serializers import BlogSerializer, BlogSlugSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = {
        'blogs',
        'blogs/<slug:slug>',
        'projects',
    }
    return Response(routes)

@api_view(['GET'])
def projects_view(request):
    projects = Project.objects.filter(show_project = True)
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def blogs_view(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many = True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getBlogSlugs(request):
    blog = Blog.objects.all()
    serializer = BlogSlugSerializer(blog, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_view(request, slug):
    try: 
        blog = Blog.objects.get(slug = slug)
        serializer = BlogSerializer(blog, many = False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({'message':"There's no blog with that name"}, status = status.HTTP_404_NOT_FOUND)
    
    