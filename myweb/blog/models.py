from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    modified_time=models.DateTimeField('修改时间',auto_now=True)

    excerpt = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title