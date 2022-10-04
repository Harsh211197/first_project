from datetime import date
from email.policy import default
from operator import truediv
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name=models.CharField(max_length=30,unique=True)
    description=models.CharField(max_length=100)
    board_date=models.DateTimeField(auto_now_add=True,null=True)
    board_starter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
         return self.name

class Topic(models.Model):
    subject=models.CharField(max_length=255)
    last_updated=models.DateTimeField(auto_now_add=True)
    board=models.ForeignKey(Board,on_delete=models.CASCADE,related_name='topics')
    starter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
         return self.subject