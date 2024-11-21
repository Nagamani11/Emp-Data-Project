from django.db import models
class EmployeesData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    percentage = models.IntegerField()
    year = models.IntegerField()
    location = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
