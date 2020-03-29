from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='recipe_pics')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.IntegerField()
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    chef = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title