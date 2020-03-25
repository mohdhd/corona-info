from django.db import models

# Create your models here.

class GStats(models.Model):
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    confirmed = models.IntegerField(default=0)


class State(models.Model):
    name = models.CharField(max_length=30)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    confirmed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    date = models.DateField()

    def __str__(self):
        return self.title
