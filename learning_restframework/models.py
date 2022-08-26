from django.db import models

# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = [("M", "male"), ("F", "female"), ("X", "secret")]

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} -- {self.age} -- {self.gender}"
