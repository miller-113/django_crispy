from django.urls import path
from .views import ProductCreateView, ProductListView


urlpatterns = [
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('product-list/', ProductListView.as_view(), name='product_list'),
]
