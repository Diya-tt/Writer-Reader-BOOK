from django.db import models
from django.contrib.auth.models import User
from writerapp.models import StoryModel

# Create your models here.


class CommentModel(models.Model):
    blog=models.ForeignKey(StoryModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.comment