from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filter import Orderfilter
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'AccountsApp/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'AccountsApp/products.html',{'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all() #Many to one relationship
    order_count = orders.count()

    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'AccountsApp/customer.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    _customer=Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=_customer)
   # form = OrderForm(initial={'customer':_customer})
    if request.method == "POST":
        print('Printing post',request.POST)
      #  form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=_customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'form':formset}
    return render(request,'AccountsApp/order_from.html',context)

def UpdateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
       # print('Printing post',request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'AccountsApp/order_from.html',context)

def deleteOrder(request,pk):
    item=Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'AccountsApp/delete.html',context)
