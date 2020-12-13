from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
# Create your models here.


class Exam(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)


    def __str__(self):
        return self.Question
    
class Solver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.user.username
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     display_name = models.CharField(max_length=20, db_index=True, default="Add your name")
#     image = models.ImageField(upload_to="profile/", db_index=True, default='profile/default.jpg')

#     def __str__(self):
#         return self.user.username

