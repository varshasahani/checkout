from django.db import models
from django.contrib.auth.models import User

product_discounts = {
    "A": [
        {"quantity": 3, "price": 130.00},
        {"quantity": 1, "price": 50.00}
    ],
    "B": [
        {"quantity": 2, "price": 45.00},
        {"quantity": 1, "price": 30.00}
    ],
    "C": [{"quantity": 1, "price": 20.00}],
    "D": [{"quantity": 1, "price": 15.00}],
}

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="cart")
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    products=models.JSONField(default=dict)

    def __str__(self):
        return f"Cart ID: {self.id}, Total Price: {self.total_price}, Products: {self.products}"

