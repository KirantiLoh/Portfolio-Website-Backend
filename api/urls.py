from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='Routes'),
    path('projects', views.projects_view, name='Projects'),
    path('blogs', views.blogs_view, name="Blogs"),
    path('blogs/slugs', views.getBlogSlugs, name="Get Blog's Slugs"),
    path('blogs/<slug:slug>', views.blog_view, name="Blog"),
]