from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostModel(models.Model):
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    caption = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=True,blank=True)
    post_image = models.ImageField(upload_to='post/media/images/',null=True,blank=True)
    def __str__(self):
        return f'post {self.caption}'
    
class PostLikeModel(models.Model):
    post = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='likes')
    like = models.PositiveIntegerField(default=0)

class PostUnlikeModel(models.Model):
    post = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='unlikes')
    unlike = models.PositiveIntegerField(default=0)

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'coomment by {self.post.caption}'