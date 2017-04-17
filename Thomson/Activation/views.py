import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Order
# -*- coding: utf-8 -*-
from Activation.form import LoginForm
# Create your views here.

def first(request):
    customers = Customer.objects.all()
    print(customers)
    return render(request, "index.html", {"customers":customers})
    #return HttpResponse('<h1>This is Hello World'+str(customers)+'</h1>')

def order(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    orders=Order.objects.all()
    return render(request,"order.html",{"orders":orders,"today":today,"days_of_week" : daysOfWeek})

def login(request):
    username = "not logged in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'login.html', {"username": username})