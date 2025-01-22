from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StoryModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=10000000000000)
    date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)
    image=models.ImageField(upload_to='media')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title