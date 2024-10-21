from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    series = models.CharField(max_length=9, blank=True, null=True)
    jshshir = models.CharField(max_length=14, blank=True, null=True)
    phone = models.CharField(max_length=13)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
