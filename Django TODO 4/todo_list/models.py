from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return self.text