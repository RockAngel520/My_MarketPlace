from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENEBLED

def get_products_from_cashe():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENEBLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_from_category(category_id):
    """Функция, которая возвращает список всех продуктов в указанной категории"""
    return Product.objects.filter(category_id=category_id)
