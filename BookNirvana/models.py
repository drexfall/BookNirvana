from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User as BaseUser
# Create your models here.


class User(BaseUser):
    profile_photo = models.FileField(upload_to="static/pps/")
    book_info = models.JSONField()
    shelves = models.JSONField()
    social_links = models.JSONField()
    bio = models.CharField(max_length=300,blank=True)
    history = HistoricalRecords()

    def get_shelf_detail(self):
        data = {}
        for shelf_id in self.shelves:
            shelf = Shelf.objects.get(id=shelf_id)
            books = {}
            for book_id in self.shelves[shelf_id]:
                book = Book.objects.get(id=book_id)
                books.update({book_id:book})
            data.update({shelf_id: {"name": shelf.name, "books": books}})
        return data

class Book(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    img = models.URLField(max_length=1000, blank=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    illustrator = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    series = models.CharField(max_length=300, blank=True)
    release_number = models.CharField(max_length=300, blank=True)
    genre = models.CharField(max_length=300)
    set_in = models.CharField(max_length=300, blank=True)
    publisher = models.CharField(max_length=300)
    publication_date = models.CharField(max_length=100)
    pages = models.CharField(max_length=300)
    isbn = models.CharField(max_length=300)
    preceded_by = models.CharField(max_length=300, blank=True)
    preceded_url = models.URLField(max_length=1000, blank=True)
    followed_by = models.CharField(max_length=300, blank=True)
    followed_url = models.URLField(max_length=1000, blank=True)
    film = models.CharField(max_length=300, blank=True)
    film_url = models.URLField(max_length=1000, blank=True)
    reviews = models.JSONField()
    like_status = models.JSONField()
    history = HistoricalRecords()

    def get_likes(self):
        count = 0
        for likes in like_status:
            if like_status[likes]:
                count += 1

        return count


class Review(models.Model):
    
    reviewer = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    comment = models.CharField(max_length=300)
    rating_choices = ((1, "Very Bad"),
                      (2, "Slightly Bad"),
                      (3, "Good"),
                      (4, "Great"),
                      (5, "Exceptional"))
    rating = models.IntegerField(choices=rating_choices)
    history = HistoricalRecords()


class Shelf(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    user_id = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=100)
    last_uploaded = models.DateField(auto_now=True)
    history = HistoricalRecords()

class Settings(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    background = models.FileField(upload_to="static",default="static/bg.png")