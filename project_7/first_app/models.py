from django.db import models

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'Name : {self.name}'
    
    