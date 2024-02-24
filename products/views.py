# views 是使用者可以看到些什麼,在哪一頁可以看到什麼
# 每一個views裡面的function都要有吃 request這個parameter
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products -> index -> main page
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products' : products})


# products/new
def new(request):
    return HttpResponse("Hi it's a product new page!!")

