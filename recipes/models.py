# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm


class Recipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=2000)
    hardness = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)])
    minutes = models.IntegerField(validators=[
        MinValueValidator(1)])
    created_by = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created_by']
        fields = ['name', 'description', 'hardness', 'minutes']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['topic', 'message']