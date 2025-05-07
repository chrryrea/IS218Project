from django.urls import path
from . import views
from . import views_cart

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    
    # Cart URLs
    path('cart/', views_cart.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views_cart.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views_cart.cart_remove, name='cart_remove'),
]
