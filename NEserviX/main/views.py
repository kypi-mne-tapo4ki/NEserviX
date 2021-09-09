from django.shortcuts import render


def index(request):
    return render(request, 'main/main.html')


def new_sale(request):
    return render(request, 'main/new_sale.html')


def all_sales(request):
    return render(request, 'main/all_sales.html')

