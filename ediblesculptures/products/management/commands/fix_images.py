from django.core.management.base import BaseCommand
from products.models import Product, Category
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Fix image paths for products and categories'

    def handle(self, *args, **options):
        # Update all categories to use the same image
        categories = Category.objects.all()
        for category in categories:
            category.image = 'category_images/bananas.png'
            category.save()
            self.stdout.write(self.style.SUCCESS(f'Updated image for category: {category.name}'))

        # Update all products to use the same image
        products = Product.objects.all()
        for product in products:
            product.image = 'product_images/bananas.png'
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Updated image for product: {product.name}'))

        self.stdout.write(self.style.SUCCESS('All images have been updated successfully'))
