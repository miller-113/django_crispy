from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return f"{self.name} ({self.quantity} count)"
