"""
Seed справочника Product ориентировочными БЖУ на 100 г.

Значения округлены по открытым справочным данным состава продуктов
(типовые таблицы / USDA FoodData Central, сырые/базовые формы).
Для демо и дипломной практики; не замена официальной маркировке.
"""

from django.core.management.base import BaseCommand

from CookAI.models import Product

# name, calories, protein, fat, carbs, category
SEED_PRODUCTS = [
    ("Куриная грудка", 165.0, 31.0, 3.6, 0.0, "птица"),
    ("Говядина постная", 250.0, 26.0, 15.0, 0.0, "мясо"),
    ("Лосось атлантический", 208.0, 20.0, 13.0, 0.0, "рыба"),
    ("Яйцо куриное", 143.0, 12.6, 9.5, 0.7, "яйца"),
    ("Молоко 2.5%", 52.0, 2.9, 2.5, 4.7, "молочка"),
    ("Творог 5%", 121.0, 17.0, 5.0, 3.0, "молочка"),
    ("Сыр твёрдый", 402.0, 25.0, 33.0, 1.3, "молочка"),
    ("Рис белый сырой", 365.0, 7.1, 0.7, 80.0, "крупы"),
    ("Гречка сырая", 343.0, 13.3, 3.4, 71.5, "крупы"),
    ("Овсяные хлопья", 389.0, 16.9, 6.9, 66.3, "крупы"),
    ("Картофель сырой", 77.0, 2.0, 0.1, 17.5, "овощи"),
    ("Морковь сырая", 41.0, 0.9, 0.2, 9.6, "овощи"),
    ("Помидор", 18.0, 0.9, 0.2, 3.9, "овощи"),
    ("Лук репчатый", 40.0, 1.1, 0.1, 9.3, "овощи"),
    ("Яблоко", 52.0, 0.3, 0.2, 13.8, "фрукты"),
    ("Банан", 89.0, 1.1, 0.3, 22.8, "фрукты"),
    ("Фасоль консервированная", 84.0, 5.5, 0.4, 15.0, "бобовые"),
    ("Чечевица сырая", 352.0, 24.6, 1.1, 63.4, "бобовые"),
    ("Масло подсолнечное", 884.0, 0.0, 100.0, 0.0, "масла"),
    ("Хлеб пшеничный", 265.0, 9.0, 3.2, 49.0, "хлеб"),
]


class Command(BaseCommand):
    help = "Заполняет справочник Product 20 продуктами с ориентировочными БЖУ на 100 г"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Удалить все Product перед загрузкой",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            deleted, _ = Product.objects.all().delete()
            self.stdout.write(f"Удалено продуктов: {deleted}")

        created = 0
        updated = 0
        for name, calories, protein, fat, carbs, category in SEED_PRODUCTS:
            _, was_created = Product.objects.update_or_create(
                name=name,
                defaults={
                    "calories": calories,
                    "protein": protein,
                    "fat": fat,
                    "carbs": carbs,
                    "category": category,
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Готово: создано {created}, обновлено {updated}, всего в seed {len(SEED_PRODUCTS)}"
            )
        )
