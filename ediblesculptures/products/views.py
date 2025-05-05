from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Product, Feedback, Category
from .forms import FeedbackForm

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    feedbacks = product.feedbacks.all()
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.product = product
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Your feedback has been submitted!')
            return redirect('product_detail', pk=pk)
    else:
        form = FeedbackForm()
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'feedbacks': feedbacks,
        'form': form
    })

@login_required
def admin_dashboard(request):
    # Get all products with their average ratings in a single query
    products_with_ratings = Product.objects.annotate(avg_rating=Avg('feedbacks__rating'))
    
    # Get recent feedbacks
    recent_feedbacks = Feedback.objects.order_by('-created_at')[:10]
    
    # Get all categories
    categories = Category.objects.all()
    
    # Prepare product ratings data
    product_ratings = [
        {
            'product': product,
            'avg_rating': product.avg_rating or 0,
            'feedback_count': product.feedbacks.count()
        }
        for product in products_with_ratings
    ]
    
    return render(request, 'products/admin_dashboard.html', {
        'product_ratings': product_ratings,
        'recent_feedbacks': recent_feedbacks,
        'categories': categories
    })
