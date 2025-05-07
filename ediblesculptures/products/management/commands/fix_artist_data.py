from django.core.management.base import BaseCommand
from django.db import connection
from products.models import Artist, Category, Product

class Command(BaseCommand):
    help = 'Fix artist data for migration'

    def handle(self, *args, **options):
        # First, let's create default artists for existing products
        with connection.cursor() as cursor:
            # Get all unique artist names from the products table
            cursor.execute("SELECT DISTINCT artist FROM products_product")
            artist_names = [row[0] for row in cursor.fetchall()]
            
            self.stdout.write(f"Found {len(artist_names)} unique artists: {artist_names}")
            
            # Create Artist objects for each artist name
            for name in artist_names:
                artist = Artist.objects.create(
                    name=name,
                    bio=f"Bio for {name}",
                    image="artist_images/default-artist.jpg",
                    featured=False
                )
                self.stdout.write(self.style.SUCCESS(f"Created artist: {artist.name} with ID {artist.id}"))
            
            # Update the schema to use integer for artist_id
            cursor.execute("ALTER TABLE products_product RENAME TO products_product_old")
            cursor.execute("""
                CREATE TABLE products_product (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(200) NOT NULL,
                    description TEXT NOT NULL,
                    price DECIMAL NOT NULL,
                    image VARCHAR(100) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    category_id INTEGER NOT NULL REFERENCES products_category (id) DEFERRABLE INITIALLY DEFERRED,
                    artist_id INTEGER NOT NULL REFERENCES products_artist (id) DEFERRABLE INITIALLY DEFERRED,
                    featured BOOL NOT NULL
                )
            """)
            
            # Copy data from old table to new table, mapping artist names to artist IDs
            for artist in Artist.objects.all():
                cursor.execute(f"""
                    INSERT INTO products_product (
                        id, name, description, price, image, created_at, updated_at, category_id, artist_id, featured
                    )
                    SELECT 
                        id, name, description, price, image, created_at, updated_at, category_id, {artist.id}, 0
                    FROM products_product_old
                    WHERE artist = ?
                """, [artist.name])
                
                count = cursor.rowcount
                self.stdout.write(f"Updated {count} products for artist {artist.name}")
            
            # Drop the old table
            cursor.execute("DROP TABLE products_product_old")
            
            self.stdout.write(self.style.SUCCESS('Successfully fixed artist data'))
