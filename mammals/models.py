from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Mammal(models.Model):
    name = models.CharField(max_length=64)
    added_by = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    scientific_name = models.CharField(max_length=64)
    population = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mammal_detail', args=[str(self.pk)])


