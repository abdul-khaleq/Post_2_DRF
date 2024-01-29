from rest_framework import serializers
from .import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostModel
        # fields = ['caption','body','post_image']
        fields = '__all__'
        
        
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLikeModel
        fields = '__all__'

class PostUnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostUnlikeModel
        fields = '__all__'

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentModel
        # fields = ['post','body']
        fields = '__all__'