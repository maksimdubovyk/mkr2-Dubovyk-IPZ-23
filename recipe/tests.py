from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Супи")
        self.category2 = Category.objects.create(name="Напої")

    def test_category_creation(self):
        soups = Category.objects.get(name="Супи")
        drinks = Category.objects.get(name="Напої")
        self.assertEqual(soups.name, "Супи")
        self.assertEqual(drinks.name, "Напої")

    def test_category_str(self):
        category = Category.objects.get(name="Супи")
        self.assertEqual(str(category), category.name)

    def test_category_iter(self):
        category = Category.objects.get(name="Супи")
        category_iter = dict(category)
        self.assertEqual(category_iter, {'name': "Супи"})

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Супи")
        self.recipe = Recipe.objects.create(
            title="Borscht",
            description="A traditional Ukrainian beet soup.",
            instructions="Cook beets, add vegetables and simmer.",
            ingredients="Beets, cabbage, potatoes, carrots, onions, garlic",
            category=self.category
        )

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(title="Borscht")
        self.assertEqual(recipe.title, "Borscht")
        self.assertEqual(recipe.description, "A traditional Ukrainian beet soup.")
        self.assertEqual(recipe.instructions, "Cook beets, add vegetables and simmer.")
        self.assertEqual(recipe.ingredients, "Beets, cabbage, potatoes, carrots, onions, garlic")
        self.assertEqual(recipe.category.name, "Супи")

    def test_recipe_str(self):
        recipe = Recipe.objects.get(title="Borscht")
        self.assertEqual(str(recipe), recipe.title)
