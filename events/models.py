from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title