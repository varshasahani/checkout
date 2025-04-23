from django.db import models

product_discounts = {
    "A": [
        {"quantity": 3, "price": 130.00},
        {"quantity": 1, "price": 50.00}
    ],
    "B": [
        {"quantity": 2, "price": 50.00},
        {"quantity": 1, "price": 30.00}
    ],
    "C": [{"quantity": 1, "price": 20.00}],
    "D": [{"quantity": 1, "price": 15.00}],
}

procusts={
    "A":"A",
    "B":"B",
    "C":"C",
    "D":"D",
}

# Create your models here.
class Cart(models.Model):
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    products=models.JSONField(default=list,choices=procusts)
    discount_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return f"Cart ID: {self.id}, Total Price: {self.total_price}, Products: {self.products}, Discount Price: {self.discount_price}"

    def get_price(product_code, quantity):
        total = 0
        discounts = sorted(product_discounts[product_code], key=lambda x: -x["quantity"])
        for d in discounts:
            qty_bundle = d["quantity"]
            bundle_price = d["price"]
            count = quantity // qty_bundle
            total += count * bundle_price
            quantity -= count * qty_bundle
        return total

    def calculate_total_price(self):
        total_price = 0.00
        hash_map = {}
        for product in self.products:
            if product in hash_map:
                hash_map[product] += 1
            else:
                hash_map[product] = 1
        for product, quantity in hash_map.items():
            total_price += self.get_price(product, quantity)
        self.discount_price = total_price
        self.total_price = total_price
        self.save()
