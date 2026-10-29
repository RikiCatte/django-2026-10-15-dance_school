from django.db import models

from schoolmanagement.models import School

__all__ = [
    "Classroom",
    "Course",
    "DayOfTheWeek"
]

class DayOfTheWeek(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.CharField(max_length=50)
    day_of_the_week = models.ForeignKey(DayOfTheWeek, on_delete=models.CASCADE, related_name="courses")
    starting_hour = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="courses")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="courses")