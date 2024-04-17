from django.db import models
from django.contrib.auth.models import  User

class Category(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()
    rasm = models.ImageField(upload_to = 'yangilik/')
    views = models.PositiveIntegerField(default = 0)
    created = models.DateTimeField(auto_now_add = True )
    muallif = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name="muallif" )
    bolim =  models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True )
    likes = models.ManyToManyField(User, related_name="Likes")


    def __str__(self):
        return self.title
        
class Comment(models.Model):
    izoh = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    muallif = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    news = models.ForeignKey( News, on_delete = models.CASCADE,related_name="comments")

