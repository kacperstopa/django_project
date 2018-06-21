from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from recipes.models import Recipe, RecipeForm, CommentForm


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def comments(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'comments.html', {'recipe': recipe})


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe', recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def userrecipes(request, username):
    user = User.objects.get(username=username)
    recipes = Recipe.objects.filter(created_by=user)
    return render(request, 'user_recipes.html', {'recipes': recipes, 'user': user})


def delete(request, pk):
    Recipe.objects.filter(pk=pk).delete()
    return redirect('home')


@login_required(login_url='login')
def add_comment(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.created_by = request.user
            comment.save()
            return redirect('comments', pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'recipe': recipe})
