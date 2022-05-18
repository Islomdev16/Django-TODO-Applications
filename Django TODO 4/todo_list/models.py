from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    added_time = models.DateTimeField()

    def __str__(self):
        return self.title