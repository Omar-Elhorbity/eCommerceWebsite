from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
def home(request):
    return render(request, 'products/home.html')

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj}
    return render(request, 'products/products.html', context)
