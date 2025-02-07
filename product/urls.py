from django.urls import path

from .views import product_view

urlpatterns = [
    path('add-product/', product_view, name='add_product'),
]
