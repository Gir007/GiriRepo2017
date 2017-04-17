from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Order
# Create your views here.

def first(request):
    customers = Customer.objects.all()
    print(customers)
    return render(request, "index.html", {"customers":customers})
    #return HttpResponse('<h1>This is Hello World'+str(customers)+'</h1>')

def order(request):
    orders=Order.objects.all()
    return render(request,"order.html",{"orders":orders})