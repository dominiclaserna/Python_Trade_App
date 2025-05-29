from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stock, Order
from .serializers import StockSerializer, OrderSerializer
from django.db.models import Sum, F

class PlaceOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class PortfolioValueView(APIView):
    """
    GET:
    - /api/portfolio/  -> total portfolio value
    - /api/portfolio/<stock_id>/ -> total value for specific stock
    """
    def get(self, request, stock_id=None):
        orders = Order.objects.all()
        if stock_id:
            orders = orders.filter(stock_id=stock_id)

        buys = orders.filter(order_type=Order.BUY).aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0

        sells = orders.filter(order_type=Order.SELL).aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0

        total_invested = buys - sells

        return Response({
            'stock_id': stock_id,
            'total_invested_value': round(total_invested, 2)
        })
