from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg
from .models import Product, Review, Category, Artist, Event
from datetime import datetime
from .forms import CartAddProductForm, ReviewForm

def home(request):
    featured_products = Product.objects.filter(featured=True)[:4]
    featured_artist = Artist.objects.filter(featured=True).first()
    upcoming_events = Event.objects.filter(date__gte=datetime.now()).order_by('date')[:3]
    
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'featured_artist': featured_artist,
        'upcoming_events': upcoming_events
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    categories = Category.objects.all()
    artists = Artist.objects.all()
    products = Product.objects.all()
    
    category_id = request.GET.get('category')
    artist_id = request.GET.get('artist')
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    if artist_id:
        products = products.filter(artist_id=artist_id)
    
    return render(request, 'products/product_list.html', {
        'categories': categories,
        'artists': artists,
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    cart_product_form = CartAddProductForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('products:product_detail', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form,
        'cart_product_form': cart_product_form
    })

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'products/artist_list.html', {
        'artists': artists
    })

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    products = artist.products.all()
    return render(request, 'products/artist_detail.html', {
        'artist': artist,
        'products': products
    })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })
