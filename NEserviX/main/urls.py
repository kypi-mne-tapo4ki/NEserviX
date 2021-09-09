from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_sale', views.new_sale),
    path('all_sales', views.all_sales),
]
