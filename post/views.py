from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = models.PostModel.objects.all()
    serializer_class = serializers.PostSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        post_id = self.request.query_params.get('post_id')
        print(post_id)
        if post_id:
            queryset = queryset.filter(id=post_id)
        return queryset
    
class PostLikeViewset(viewsets.ModelViewSet):
    queryset = models.PostLikeModel.objects.all()
    serializer_class = serializers.PostLikeSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        post_id = self.request.query_params.get('id')
        print(post_id)
        if post_id:
            queryset = queryset.filter(id=post_id)
        return queryset

class PostUnlikeViewset(viewsets.ModelViewSet):
    queryset = models.PostUnlikeModel.objects.all()
    serializer_class = serializers.PostUnlikeSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.CommentModel.objects.all()
    serializer_class = serializers.PostCommentSerializer
