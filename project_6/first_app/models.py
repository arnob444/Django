from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(null= True)
    fathers_name = models.TextField(default= "Ratan Chandra Das")


    def __str__(self) -> str:
        return f"Roll no : {self.roll} - {self.name}" 