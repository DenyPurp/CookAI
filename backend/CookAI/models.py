from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        VEGETABLES = "овощи", "Овощи"
        FRUITS = "фрукты", "Фрукты"
        GRAINS = "крупы", "Крупы"
        MEAT = "мясо", "Мясо"
        POULTRY = "птица", "Птица"
        FISH = "рыба", "Рыба"
        DAIRY = "молочка", "Молочка"
        EGGS = "яйца", "Яйца"
        OILS = "масла", "Масла"
        LEGUMES = "бобовые", "Бобовые"
        BREAD = "хлеб", "Хлеб"

    name = models.CharField(max_length=200)
    calories = models.FloatField(help_text="ккал на 100 г")
    protein = models.FloatField(help_text="белки, г на 100 г")
    fat = models.FloatField(help_text="жиры, г на 100 г")
    carbs = models.FloatField(help_text="углеводы, г на 100 г")
    category = models.CharField(max_length=100, choices=Category.choices)

    class Meta:
        db_table = "Products"
        ordering = ["name"]

    def __str__(self):
        return self.name
