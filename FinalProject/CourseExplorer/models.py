from django.db import models
from django.contrib.auth.models import User

class user_mod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class KooferData(models.Model): 
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    num_ratings = models.IntegerField(default=0)
    gpa = models.FloatField(default=0.0)
    
class CourseExplorerData(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=100)
    description = models.TextField()


class RateMyProfessor(models.Model):
    avg_rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)
    instructor = models.ForeignKey(CourseExplorerData, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
