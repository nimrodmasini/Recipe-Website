from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipes
from django.contrib import messages
from .forms import RecipesForm
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))

    else:
        form = RecipesForm()

    context = {
        "form":form
    }
    return render(request, 'create_recipe.html', context)

def view_recipe(request):
    recipes = Recipes.objects.all()
    context = {
        "recipes" : recipes
    }
    return render(request, 'view_recipe.html', context)

def recipe_details(request, pk):
    recipes = get_object_or_404(Recipes, pk=pk)
    context = {
        "recipes" : recipes
    }
    return render(request, 'recipe_details.html', context)


