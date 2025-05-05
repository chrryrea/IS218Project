from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from pathlib import Path
import shutil
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Imports original content from the HTML project'

    def handle(self, *args, **options):
        # Create categories
        categories = [
            {'name': 'Dishware', 'image': 'images/plates.jpg'},
            {'name': 'Pottery', 'image': 'images/pottery.jpg'},
            {'name': 'Sculpture', 'image': 'images/spikes.jpg'},
            {'name': 'Home Decor', 'image': 'images/home.jpg'},
            {'name': 'Wall Decor', 'image': 'images/wall.jpg'}
        ]

        # Copy images and create categories
        for category_data in categories:
            category = Category.objects.create(
                name=category_data['name']
            )
            
            # Copy category image
            original_path = Path(r'C:\Users\Ian\Downloads\IS218-groupProject-main\IS218-groupProject-main') / category_data['image']
            destination_path = Path(r'C:\Users\Ian\IS218Project\ediblesculptures\products\static\products\images') / Path(category_data['image']).name
            shutil.copy2(original_path, destination_path)
            
            # Save image to category
            with open(destination_path, 'rb') as f:
                category.image.save(
                    Path(category_data['image']).name,
                    ImageFile(f)
                )
            
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Create products
        products = [
            {
                'name': 'Mixed Fruit',
                'description': '"Mixed Fruit" by Samantha Fox is a playful edible sculpture combining a variety of fruits into a colorful, flowing arrangement. It captures a sense of movement, freshness, and fleeting beauty.',
                'price': 213.78,
                'image': 'images/mixedf.webp',
                'artist': 'Samantha Fox',
                'category': 'Sculpture'
            },
            {
                'name': 'Exotic Fruit Spike',
                'description': '"Exotic Fruit Spike" by Sophia Bennet features an energetic display of tropical fruits arranged around sharp, vertical elements. The sculpture blends bold shapes and vibrant colors to create a striking sense of contrast and motion.',
                'price': 345.99,
                'image': 'images/spikes.jpg',
                'artist': 'Sophia Bennet',
                'category': 'Sculpture'
            },
            {
                'name': 'Polished Pears',
                'description': '"Polished Pears" by Samantha Fox showcases a cluster of gleaming pears, arranged to emphasize balance, purity, and the subtle beauty found in everyday forms.',
                'price': 186.79,
                'image': 'images/polished.webp',
                'artist': 'Samantha Fox',
                'category': 'Sculpture'
            },
            {
                'name': 'Mixed Media',
                'description': '"Miked Media" by Dan Potter blends everyday objects with edible elements, creating a layered composition that explores sound, texture, and fleeting moments.',
                'price': 106.89,
                'image': 'images/mixedm.png',
                'artist': 'Dan Potter',
                'category': 'Sculpture'
            },
            {
                'name': 'Fruity Dishes',
                'description': '"Fruity Dishes" by Samantha Fox features a series of hand-sculpted plates, each uniquely shaped to cradle vibrant arrangements of fresh fruit. The work highlights the interplay between crafted forms and natural abundance, inviting viewers to appreciate the artistry in both the vessel and what it holds.',
                'price': 118.78,
                'image': 'images/plates.jpg',
                'artist': 'Samantha Fox',
                'category': 'Dishware'
            },
            {
                'name': 'Pair of Pears',
                'description': '"Pair of Pears " by Jacob Sullivan is a sculptural artwork featuring two pears, likely crafted to explore form, texture, and natural elegance. The piece embodies simplicity and organic beauty, inviting viewers to appreciate everyday objects as art.',
                'price': 324.99,
                'image': 'images/pairofpear.jpg',
                'artist': 'Jacob Sullivan',
                'category': 'Sculpture'
            },
            {
                'name': 'Red Strawberry',
                'description': '"Red Strawberry" by Samantha Fox centers on a single oversized strawberry, sculpted with vivid detail to capture both the fragility and intensity of natural beauty.',
                'price': 246.89,
                'image': 'images/redstrawberry.jpg',
                'artist': 'Samantha Fox',
                'category': 'Sculpture'
            },
            {
                'name': 'Cool Green Pear',
                'description': '"Cool Green Pears" by Jacob Sullivan features a collection of smooth, stylized pears in gentle green shades, creating a calm, refreshing atmosphere through simple, organic forms.',
                'price': 231.78,
                'image': 'images/cool.jpg',
                'artist': 'Jacob Sullivan',
                'category': 'Sculpture'
            }
        ]

        # Copy and create products
        for product_data in products:
            category = Category.objects.get(name=product_data['category'])
            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                artist=product_data['artist'],
                category=category
            )
            
            # Copy product image
            original_path = Path(r'C:\Users\Ian\Downloads\IS218-groupProject-main\IS218-groupProject-main') / product_data['image']
            destination_path = Path(r'C:\Users\Ian\IS218Project\ediblesculptures\products\static\products\images') / Path(product_data['image']).name
            shutil.copy2(original_path, destination_path)
            
            # Save image to product
            with open(destination_path, 'rb') as f:
                product.image.save(
                    Path(product_data['image']).name,
                    ImageFile(f)
                )
            
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
