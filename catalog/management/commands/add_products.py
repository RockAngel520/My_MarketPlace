from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Смартфоны', description='Лучшие смартфоны по доступным ценам')

        phones = [
            {'name': 'Ipone', 'description': '256 Gb', 'price': 100000, 'category': category, 'is_publish': True},
            {'name': 'Samsung', 'description': '128 Gb', 'price': 80000, 'category': category, 'is_publish': True},
        ]

        for phone_data in phones:
            phone, created = Product.objects.get_or_create(**phone_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added phone: {phone.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Phone already exists: {phone.name}'))
