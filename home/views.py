from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def add(request):
    if request.method == 'POST':
        f = ProductForm(request.POST)
        if f.is_valid():
            f.save()
            print('added sucessfully')
            msg = "added successfully"
            form = ProductForm()
            return render(request,'home/add.html',{'msg':msg,'form':form})
        else:
            print('error in saving')
    else:
        form = ProductForm()
        return render(request,'home/add.html',{'form':form})


def home(request):
    data = Product.objects.all()
    return render(request,'home/home.html',{'data':data})

def update(request,pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            msg = 'Data Updated Successfully'
            data = Product.objects.all()
            return render(request,'home/home.html',{'data':data,'msg':msg})
    else:
        product = Product.objects.get(id=pk)
        form = ProductForm(instance=product)
        return render(request,'home/update.html',{'form':form,'id':pk})
     