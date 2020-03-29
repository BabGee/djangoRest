from django.shortcuts import render
from .models import Recipe, Category

def index(request):
    all_recipes = Recipe.objects.all()
    context = {
        'recipes': all_recipes,
        '4recipes': all_recipes[:4]
    }
    return render(request, 'recipe/index.html', context)

def recipe_detail(request, pk):
    context = {
        'recipe' : Recipe.objects.get(pk=pk)
    }
    return render(request, 'recipe/recipes_details.html', context)  