from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    ORDER_TYPE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type} {self.quantity} of {self.stock.name} at {self.price}"
