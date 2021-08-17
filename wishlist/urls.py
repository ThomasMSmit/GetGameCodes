from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('add/<int:product_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<int:product_id>', views.delete_from_wishlist, name='delete_from_wishlist'),
]
