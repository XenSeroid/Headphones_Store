from django.shortcuts import render, get_object_or_404
from product.models import Headphones

def index(request):
    h = Headphones.objects.all()
    
    return render(request,'Headphones.html',{'headphones':h,})

def detail(request, headphones_id):
    h = get_object_or_404(Headphones, id = headphones_id)
    return render(request,'headphones_detail.html',{'headphone':h})


def headphones(request):
    return render(request,'B&W px8.html')

def headphones1(request):
    return render(request,'Bang & Olufsen Beoplay H95.html')

def headphones2(request):
    return render(request,'Apple Airpods Max.html')

def headphones3(request):
    return render(request,'Sennheiser HD 400 PRO.html')

def headphones4(request):
    return render(request,'Apple AirPods Pro 3 gen.html')
