from django.db import models

class Post(models.Model):
    name = models.CharField(default='request.user',max_length=150,null=True)
    photo = models.ImageField(default='lord.jpg',null=True)
    description = models.TextField(null=True)

def __str__ (self):
    return self.description
