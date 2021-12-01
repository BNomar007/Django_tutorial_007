from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from recipes.models import Recipe, RecipeIngredient
from .models import Meal, MealStatus

User = get_user_model()


class MealTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('raulgane', password='123321')
        self.user_id = self.user_a.id

        self.recipe_a = Recipe.objects.create(
            name = 'Tacos',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name = 'Grilled Chicken',
            user = self.user_a
        )
        self.recipe_c = Recipe.objects.create(
            name = 'Margeritta',
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
        self.meal = Meal.objects.create(
            user = self.user_a,
            recipe = self.recipe_a
        )
        meal_b = Meal.objects.create(
            user = self.user_a,
            recipe = self.recipe_a,
            status = MealStatus.COMPLETED
        )

    def test_pending_meals(self):
        qs = Meal.objects.all().pending()
        self.assertEqual(qs.count(), 1)
        qs2 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(), 1)

    def test_completed_meals(self):
        qs = Meal.objects.all().completed()
        self.assertEqual(qs.count(), 1)
        qs2 = Meal.objects.by_user_id(self.user_id).completed()
        self.assertEqual(qs2.count(), 1)

    def test_add_with_toggle(self):
        meal_b = Meal.objects.create(
            user = self.user_a,
            recipe = self.recipe_a
        )
        qs2 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(), 2)

        added = Meal.objects.toggle_in_queue(self.user_id, self.recipe_c.id)
        qs3 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs3.count(), 3)
        self.assertTrue(added)

    def test_remove_with_toggle(self):
        added = Meal.objects.toggle_in_queue(self.user_id, self.recipe_a.id)
        qs3 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs3.count(), 0)
        self.assertFalse(added)
