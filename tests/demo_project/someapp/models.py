from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)


class Event(models.Model):
    title = models.CharField(max_length=100)
    category = models.OneToOneField(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField()
    end_date = models.DateField()
    comment = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    def __save__(self, *args, **kwargs):
        self.full_clean()
        super().save()


class Client(models.Model):
    key = models.CharField(max_length=20, unique=True)
