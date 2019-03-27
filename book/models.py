from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)


def default_category():
    return Category.objects.get(pk=4)


