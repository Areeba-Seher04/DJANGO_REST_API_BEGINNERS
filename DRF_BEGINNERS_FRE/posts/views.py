from django.shortcuts import render
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	CreateAPIView,
	UpdateAPIView,
	DestroyAPIView
	)
from rest_framework.permissions import AllowAny, IsAuthenticated 
from posts.models import Author, Post
from posts.serializers import PostSerializer, PostCreateSerializer, AuthorSerializer

#for list frontend
def home(request):
	return render(request, "index.html")

#for detail frontend
def post_detail(request, pk):
	return render(request, "post_detail.html")


#create list, detail, create, delete, update view

class AuthorDetailView(RetrieveAPIView):
	permission_classes = (AllowAny, )
	serializer_class = AuthorSerializer
	queryset = Author.objects.all()

class PostListView(ListAPIView):
	permission_classes = (AllowAny, )
	serializer_class = PostSerializer
	queryset = Post.objects.all()

class PostCreateView(CreateAPIView):
	permission_classes = (AllowAny, )
	serializer_class = PostCreateSerializer
	queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
	permission_classes = (AllowAny, )
	serializer_class = PostSerializer
	queryset = Post.objects.all()

class PostUpdateView(UpdateAPIView):
	permission_classes = (AllowAny, )
	serializer_class = PostCreateSerializer
	queryset = Post.objects.all()

class PostDeleteView(DestroyAPIView):
	permission_classes = (AllowAny, )
	queryset = Post.objects.all()