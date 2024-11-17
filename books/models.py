from django.db import models
from django.contrib.auth.models import User

from moviesite import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)  
    release_year = models.IntegerField()
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    poster_url = models.URLField()  
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

