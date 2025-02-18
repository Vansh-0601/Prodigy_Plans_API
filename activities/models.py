from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.CharField(max_length=50)  # e.g., "1x/Day", "2x/Week"
    day = models.IntegerField()  # e.g., 17, 18, etc.
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

