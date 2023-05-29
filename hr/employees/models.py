from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    category = models.ForeignKey(
        Category, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.name