from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Импорты наших представлений
from .views import health_check  # или откуда он у тебя импортируется
from CookAI.views import ProductViewSet  # <--- Импортируем наш ViewSet

# Создаем роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health_check'),

    # Подключаем все URL-адреса, сгенерированные роутером
    path('api/', include(router.urls)),
]