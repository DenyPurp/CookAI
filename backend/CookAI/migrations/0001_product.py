from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("calories", models.FloatField(help_text="ккал на 100 г")),
                ("protein", models.FloatField(help_text="белки, г на 100 г")),
                ("fat", models.FloatField(help_text="жиры, г на 100 г")),
                ("carbs", models.FloatField(help_text="углеводы, г на 100 г")),
                ("category", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "Products",
                "ordering": ["name"],
            },
        ),
    ]
