from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    body = models.TextField()
    date = models.DateField( auto_now_add=True)
    image = models.ImageField(default='default.jpg',blank=True)
    
    

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + " ..."