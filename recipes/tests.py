from django.test import TestCase
from .models import Recipe, RecipeIngredient
from .admin import User


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('raulgane', password='123321')
        self.recipe_a = Recipe.objects.create(
            name = 'Tacos',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name = 'Grilled Chicken',
            user = self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = 'Grilled Chicken',
            quantity = '2 1/2',
            unit = 'pound'
        )
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe = self.recipe_b,
            name = 'seafood salad',
            quantity = 'abc',
            unit = 'kg'
        )

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)
