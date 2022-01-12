from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['slug']