from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title
