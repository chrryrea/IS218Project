from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from products.models import Category, Artist, Product, Review, Event
import os
import datetime

class Command(BaseCommand):
    help = 'Create sample data for the Edible Sculptures website'

    def handle(self, *args, **options):
        # Create categories
        self.stdout.write('Creating categories...')
        categories = [
            {
                'name': 'Dishware',
                'description': 'Beautiful edible dishware for your table',
                'image': 'category_images/plates.jpg'
            },
            {
                'name': 'Pottery',
                'description': 'Handcrafted edible pottery pieces',
                'image': 'category_images/pottery.jpg'
            },
            {
                'name': 'Sculpture',
                'description': 'Artistic edible sculptures',
                'image': 'category_images/fruits-scultpute.webp'
            },
            {
                'name': 'Home Decor',
                'description': 'Edible decorations for your home',
                'image': 'category_images/home.jpg'
            },
            {
                'name': 'Wall Decor',
                'description': 'Edible art for your walls',
                'image': 'category_images/wall.jpg'
            }
        ]
        
        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={
                    'description': category_data['description'],
                    'image': category_data['image']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
            else:
                self.stdout.write(f'Category already exists: {category.name}')
        
        # Create artists
        self.stdout.write('Creating artists...')
        artists = [
            {
                'name': 'Samantha Fox',
                'bio': 'Samantha has been creating edible sculptures for over 10 years. Her work combines organic shapes with vibrant colors to create stunning pieces that are both visually appealing and delicious.',
                'image': 'artist_images/default-artist.jpg',
                'featured': True
            },
            {
                'name': 'Jacob Sullivan',
                'bio': 'Jacob specializes in fruit-based sculptures that highlight the natural beauty of seasonal produce. His work has been featured in numerous food art exhibitions around the country.',
                'image': 'artist_images/default-artist.jpg',
                'featured': False
            },
            {
                'name': 'Sophia Bennett',
                'bio': 'Sophia brings a background in traditional ceramics to her edible creations. Her pieces often blur the line between functional dishware and artistic expression.',
                'image': 'artist_images/default-artist.jpg',
                'featured': False
            },
            {
                'name': 'Dan Potter',
                'bio': 'Dan is known for his innovative techniques and use of unexpected ingredients. His sculptures challenge perceptions of what edible art can be.',
                'image': 'artist_images/default-artist.jpg',
                'featured': False
            }
        ]
        
        for artist_data in artists:
            artist, created = Artist.objects.get_or_create(
                name=artist_data['name'],
                defaults={
                    'bio': artist_data['bio'],
                    'image': artist_data['image'],
                    'featured': artist_data['featured']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created artist: {artist.name}'))
            else:
                self.stdout.write(f'Artist already exists: {artist.name}')
        
        # Create products
        self.stdout.write('Creating products...')
        products = [
            {
                'name': 'Mixed Fruit',
                'description': 'A beautiful arrangement of mixed fruit sculptures, perfect for a centerpiece or special occasion.',
                'price': 149.99,
                'image': 'product_images/mixedf.webp',
                'category': 'Sculpture',
                'artist': 'Samantha Fox',
                'featured': True
            },
            {
                'name': 'Exotic Fruit Spike',
                'description': 'An exotic arrangement of fruit sculptures with a dramatic spiked design.',
                'price': 199.99,
                'image': 'product_images/spikes.jpg',
                'category': 'Sculpture',
                'artist': 'Jacob Sullivan',
                'featured': True
            },
            {
                'name': 'Polished Pears',
                'description': 'Elegant pear sculptures with a polished finish, perfect for kitchen decor.',
                'price': 89.99,
                'image': 'product_images/polished.webp',
                'category': 'Home Decor',
                'artist': 'Sophia Bennett',
                'featured': False
            },
            {
                'name': 'Mixed Media',
                'description': 'A mixed media piece combining various fruit and vegetable sculptures in a harmonious arrangement.',
                'price': 249.99,
                'image': 'product_images/mixedm.png',
                'category': 'Wall Decor',
                'artist': 'Dan Potter',
                'featured': True
            },
            {
                'name': 'Fruity Dishes',
                'description': 'A set of edible dishes crafted to look like various fruits. Functional and beautiful.',
                'price': 129.99,
                'image': 'product_images/plates.jpg',
                'category': 'Dishware',
                'artist': 'Sophia Bennett',
                'featured': False
            },
            {
                'name': 'Pair of Pears',
                'description': 'A pair of beautifully crafted pear sculptures, perfect as a gift or home accent.',
                'price': 79.99,
                'image': 'product_images/pairofpear.jpg',
                'category': 'Home Decor',
                'artist': 'Jacob Sullivan',
                'featured': True
            },
            {
                'name': 'Red Strawberry',
                'description': 'A vibrant red strawberry sculpture with incredible detail and texture.',
                'price': 59.99,
                'image': 'product_images/redstrawberry.jpg',
                'category': 'Sculpture',
                'artist': 'Samantha Fox',
                'featured': False
            },
            {
                'name': 'Cool Green Pear',
                'description': 'A cool green pear sculpture with a modern twist on a classic fruit.',
                'price': 69.99,
                'image': 'product_images/cool.jpg',
                'category': 'Sculpture',
                'artist': 'Dan Potter',
                'featured': False
            }
        ]
        
        for product_data in products:
            category = Category.objects.get(name=product_data['category'])
            artist = Artist.objects.get(name=product_data['artist'])
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'image': product_data['image'],
                    'category': category,
                    'artist': artist,
                    'featured': product_data['featured']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(f'Product already exists: {product.name}')
        
        # Create reviews
        self.stdout.write('Creating reviews...')
        reviews = [
            {
                'product': 'Pair of Pears',
                'name': 'Emily Johnson',
                'email': 'emily@example.com',
                'rating': 5,
                'comment': 'Absolutely stunning! These pears look so realistic yet artistic. They\'ve become a conversation piece in my home.'
            },
            {
                'product': 'Pair of Pears',
                'name': 'Michael Smith',
                'email': 'michael@example.com',
                'rating': 4,
                'comment': 'Gorgeous and unique! I bought these for a wedding gift and the couple loved them. Would definitely recommend.'
            },
            {
                'product': 'Mixed Fruit',
                'name': 'Sarah Williams',
                'email': 'sarah@example.com',
                'rating': 5,
                'comment': 'Exquisite craftsmanship! The detail in each piece is incredible, and they look amazing as a centerpiece on my dining table.'
            },
            {
                'product': 'Exotic Fruit Spike',
                'name': 'David Brown',
                'email': 'david@example.com',
                'rating': 4,
                'comment': 'Very impressive piece! The colors are vibrant and the design is eye-catching. I\'ve received many compliments.'
            }
        ]
        
        for review_data in reviews:
            product = Product.objects.get(name=review_data['product'])
            
            review, created = Review.objects.get_or_create(
                product=product,
                name=review_data['name'],
                defaults={
                    'email': review_data['email'],
                    'rating': review_data['rating'],
                    'comment': review_data['comment']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created review by {review.name} for {product.name}'))
            else:
                self.stdout.write(f'Review already exists by {review.name} for {product.name}')
        
        # Create events
        self.stdout.write('Creating events...')
        events = [
            {
                'title': 'Annual Local Artist Fundraiser',
                'description': 'Join us for our annual fundraiser to support local artists. The event will feature live demonstrations, auctions, and refreshments. All proceeds go to supporting emerging artists in our community.',
                'date': datetime.date(2025, 10, 15)
            },
            {
                'title': 'Summer Sculpture Workshop',
                'description': 'Learn the art of edible sculpture in this hands-on workshop led by our featured artists. Perfect for beginners and experienced artists alike.',
                'date': datetime.date(2025, 7, 20)
            },
            {
                'title': 'Holiday Exhibition Opening',
                'description': 'Celebrate the holiday season with the opening of our special exhibition featuring festive edible sculptures and seasonal designs.',
                'date': datetime.date(2025, 12, 5)
            }
        ]
        
        for event_data in events:
            event, created = Event.objects.get_or_create(
                title=event_data['title'],
                defaults={
                    'description': event_data['description'],
                    'date': event_data['date']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created event: {event.title}'))
            else:
                self.stdout.write(f'Event already exists: {event.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample data'))
