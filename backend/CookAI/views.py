from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API для работы с продуктами.
    Автоматически предоставляет GET, POST, PUT, PATCH, DELETE.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer