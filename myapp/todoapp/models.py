from django.db import models
from datetime import date

# Create your models here.

class Note(models.Model):
    noteheading = models.CharField(max_length=200 , default="Untitled note")
    note = models.CharField(max_length=200)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.noteheading} - {self.note}"
