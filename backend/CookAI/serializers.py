from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Поле для красивого отображения названия категории (Овощи вместо vegetables)
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'calories',
            'protein',
            'fat',
            'carbs',
            'category',
            'category_display' # Добавляем в вывод
        ]