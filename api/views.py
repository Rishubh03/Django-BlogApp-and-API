from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostApiView(generics.ListAPIView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	serializer_class = PostSerializer
