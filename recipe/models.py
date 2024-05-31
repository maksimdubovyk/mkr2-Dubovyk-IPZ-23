from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __iter__(self):
        yield 'name', self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title
