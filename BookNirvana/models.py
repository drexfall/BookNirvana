from django.db import models
from django.contrib.auth.models import User as BaseUser
# Create your models here.

class User(BaseUser):
    shelves = models.JSONField()
    
class Book(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    img = models.URLField(max_length=1000, blank=True)
    title = models.CharField(max_length = 300)
    author = models.CharField(max_length= 300)
    illustrator = models.CharField(max_length= 300)
    country = models.CharField(max_length= 300)
    language = models.CharField(max_length= 300)
    series = models.CharField(max_length= 300, blank=True)
    release_number = models.CharField(max_length= 300, blank=True)
    genre = models.CharField(max_length= 300)
    set_in = models.CharField(max_length= 300, blank=True)
    publisher = models.CharField(max_length= 300)
    publication_date = models.CharField(max_length=100)
    pages = models.CharField(max_length= 300)
    isbn = models.CharField(max_length= 300)
    preceded_by = models.CharField(max_length= 300, blank=True)
    preceded_url = models.URLField(max_length=1000, blank=True)
    followed_by = models.CharField(max_length= 300, blank=True)
    followed_url = models.URLField(max_length=1000, blank=True)
    film = models.CharField(max_length= 300, blank=True)
    film_url = models.URLField(max_length=1000, blank=True)
    

class Shelf(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    user_id = models.ForeignKey(User, models.CASCADE)
    books = models.JSONField()