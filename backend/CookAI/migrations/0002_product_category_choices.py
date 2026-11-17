from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CookAI", "0001_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("овощи", "Овощи"),
                    ("фрукты", "Фрукты"),
                    ("крупы", "Крупы"),
                    ("мясо", "Мясо"),
                    ("птица", "Птица"),
                    ("рыба", "Рыба"),
                    ("молочка", "Молочка"),
                    ("яйца", "Яйца"),
                    ("масла", "Масла"),
                    ("бобовые", "Бобовые"),
                    ("хлеб", "Хлеб"),
                ],
                max_length=100,
            ),
        ),
    ]
