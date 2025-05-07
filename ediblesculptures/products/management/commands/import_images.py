import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from products.models import Product, Category

class Command(BaseCommand):
    help = 'Import images from original project'

    def handle(self, *args, **options):
        # Source directories
        pictures_dir = r'c:\Users\Ian\Downloads\IS218-groupProject-main\IS218-groupProject-main\Pictures'
        images_dir = r'c:\Users\Ian\Downloads\IS218-groupProject-main\IS218-groupProject-main\images'
        
        # Target directories
        category_images_dir = os.path.join(settings.MEDIA_ROOT, 'category_images')
        product_images_dir = os.path.join(settings.MEDIA_ROOT, 'product_images')
        
        # Ensure target directories exist
        os.makedirs(category_images_dir, exist_ok=True)
        os.makedirs(product_images_dir, exist_ok=True)
        
        # Category images mapping
        category_images = {
            'Dishware': 'plates.jpg',
            'Pottery': 'pottery.jpg',
            'Sculpture': 'fruits-scultpute.webp',
            'Home Decor': 'home.jpg',
            'Wall Decor': 'wall.jpg'
        }
        
        # Product images mapping
        product_images = {
            'Mixed Fruit': 'mixedf.webp',
            'Exotic Fruit Spike': 'spikes.jpg',
            'Polished Pears': 'polished.webp',
            'Mixed Media': 'mixedm.png',
            'Fruity Dishes': 'plates.jpg',
            'Pair of Pears': 'pairofpear.jpg',
            'Red Strawberry': 'redstrawberry.jpg',
            'Cool Green Pear': 'cool.jpg'
        }
        
        # Copy category images
        for category_name, image_name in category_images.items():
            source_path = os.path.join(images_dir, image_name)
            if os.path.exists(source_path):
                target_path = os.path.join(category_images_dir, image_name)
                shutil.copy2(source_path, target_path)
                self.stdout.write(self.style.SUCCESS(f'Copied {image_name} to category_images'))
                
                # Update category in database
                categories = Category.objects.filter(name=category_name)
                if categories.exists():
                    category = categories.first()
                    category.image = f'category_images/{image_name}'
                    category.save()
                    self.stdout.write(self.style.SUCCESS(f'Updated image for category: {category_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Image {image_name} not found for category {category_name}'))
        
        # Copy product images
        for product_name, image_name in product_images.items():
            source_path = os.path.join(images_dir, image_name)
            if os.path.exists(source_path):
                target_path = os.path.join(product_images_dir, image_name)
                shutil.copy2(source_path, target_path)
                self.stdout.write(self.style.SUCCESS(f'Copied {image_name} to product_images'))
                
                # Update product in database
                products = Product.objects.filter(name=product_name)
                if products.exists():
                    product = products.first()
                    product.image = f'product_images/{image_name}'
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'Updated image for product: {product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Image {image_name} not found for product {product_name}'))
        
        # Copy additional images from Pictures directory
        for filename in os.listdir(pictures_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif')):
                source_path = os.path.join(pictures_dir, filename)
                target_path = os.path.join(product_images_dir, filename)
                shutil.copy2(source_path, target_path)
                self.stdout.write(self.style.SUCCESS(f'Copied additional image {filename} to product_images'))
        
        self.stdout.write(self.style.SUCCESS('All images have been imported successfully'))
