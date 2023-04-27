from django.db import models
from django.core import validators
# Create your models here.



class Topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True,validators=[validators.MaxLengthValidator(10)])
    def __str__(self):
        return self.topic_name

class Player(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    age=models.IntegerField(validators=[validators.MinValueValidator(18)])
    play_type=models.CharField(max_length=30)

    def __str__(self):
        return self.topic_name