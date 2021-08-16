from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('pc_products', views.pc_products, name='pc_products'),
    path('psn_products', views.psn_products, name='psn_products'),
    path('xbox_products', views.xbox_products, name='xbox_products'),
    path('nintendo_products', views.nintendo_products, name='nintendo_products'),
    path('sale_products', views.sale_products, name='sale_products'),
]
