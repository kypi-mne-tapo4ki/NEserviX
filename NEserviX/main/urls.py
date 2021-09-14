from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_sale', views.new_sale, name='new_sale'),
    path('all_sales', views.all_sales, name='all_sales'),
    path('all_orders', views.all_orders, name='all_orders'),
]
