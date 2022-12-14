from django.db import models


class UserFace(models.Model):
    name = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="face-data/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url


class Service(models.Model):
    name = models.CharField(max_length=56, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=128)
    employee_id = models.CharField(max_length=20, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)
