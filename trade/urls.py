from django.urls import path
from .views import PlaceOrderView, PortfolioValueView

urlpatterns = [
    path('orders/', PlaceOrderView.as_view(), name='place_order'),
    path('portfolio/', PortfolioValueView.as_view(), name='portfolio_value'),
    path('portfolio/<int:stock_id>/', PortfolioValueView.as_view(), name='portfolio_value_stock'),
]
