import imp
import re
from django.shortcuts import render
from .forms import CardForm
from .models import Cards

# Create your views here.
def sales(request):
    data = Cards.objects.all()
    return render(request,'didac/sales.html',{'data':data})

def civom(request):
    if request.method == 'POST':
        form = CardForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('data saved')
            form = CardForm()
            return render(request,'didac/civom.html',{'form':form})
    else:
        form = CardForm()
        return render(request,'didac/civom.html',{'form':form})