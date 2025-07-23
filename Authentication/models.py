from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100, null=True)
    bio=models.TextField(max_length=100, blank=True, null= True)
    create_at=models.DateField(null=True)

    def __str__(self):
        return self.fullname


