from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'cities'
class Question(models.Model):
    question = models.CharField(max_length=250)
    vote_count = models.IntegerField(default=0)
    views = models.CharField(max_length=20)
    tags = models.CharField(max_length=250)

    def __str__(self):
        return self.question