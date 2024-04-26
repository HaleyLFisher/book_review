from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    synopsis = models.TextField()
    year_published = models.IntegerField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse("book_detail", kwargs={"pk": self.pk})
    @property
    def number_of_reviews(self):
        return Review.objects.filter(book=self).count()

class Review(models.Model):
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices, default=1)
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    user = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.title)