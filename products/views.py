from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
import pyqrcode 
import png 
from pyqrcode import QRCode 
import os
import shutil
# Create your views here.
def main(request):
    product = Product.objects.all()
    return render(request,'main.html',{'product':product})
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print("sucess")
            data= form.cleaned_data['name']
            if Product.objects.filter(name=data).exists():
                print("item already exist")
                return HttpResponse("<h1>item already exist please enter new name<h1>")
            form.save()
            a=request.get_host()
            print(a+"/"+data)
            data = str(data)
            url = pyqrcode.create("http://"+a+"/"+data) 
            url.png(data+".png",scale=6)
            shutil.move(data+".png","./media/QR_images/" + data + ".png")
            #path = "./media/QR_images/" + data + ".png"
            path = "QR_images/" + data + ".png"
            qr = Qr.objects.create(name= data,image=path)
            qr.save()
            qr = Qr.objects.filter(name=data)
            product = Product.objects.filter(name=data)
            return render(request,'qr.html',{'qr' : qr,'product':product})
        else:
            form = ProductForm()
            return render(request, 'home.html',{'form' : form}) 
    else:
        form = ProductForm()
        return render(request, 'home.html',{'form' : form})

def index(request,string):
    if Product.objects.filter(name=string).exists():
        product = Product.objects.filter(name=string)
        return render(request,'product.html',{'product':product})
    else:
        print('not found in exists')
        return HttpResponse("error page not found , please check if the object exist")

def allInfo(request,string):
    product = Product.objects.filter(name=string)
    qr = Qr.objects.filter(name=string)
    return render(request,'qr.html',{'product':product,'qr':qr})
        