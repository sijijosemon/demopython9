from django.db import models

class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

