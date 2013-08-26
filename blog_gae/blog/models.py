from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    def __unicode__(self):
         return self.name

 
class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author)
    body = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    def __unicode__(self):
         return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

 
