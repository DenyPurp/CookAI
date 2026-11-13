from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField(help_text="ккал на 100 г")
    protein = models.FloatField(help_text="белки, г на 100 г")
    fat = models.FloatField(help_text="жиры, г на 100 г")
    carbs = models.FloatField(help_text="углеводы, г на 100 г")
    category = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
