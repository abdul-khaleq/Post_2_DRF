from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.PostModel)
admin.site.register(models.PostLikeModel)
admin.site.register(models.PostUnlikeModel)
admin.site.register(models.CommentModel)