from django import forms
from .models import Recipes

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('name', 'description', 'ingredients', 'instructions', 'cooking_time')

    def save(self, commit=True):
        recipe = super(RecipesForm, self).save(commit=True)
        if commit:
            recipe.save()
        return recipe
