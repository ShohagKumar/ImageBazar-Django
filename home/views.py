from django.shortcuts import render, redirect
from home.models import Catagory
from home.models import Image

# Create your views here.


def home(request):
    catagory = Catagory.objects.all()

    pics = Image.objects.all()

    show = {
        "catagory": catagory,
        "pics": pics

    }

    return render(request, 'home.html', show)


def show_catagory(request, cid):
    catagory = Catagory.objects.all()

    cata = Catagory.objects.get(pk=cid)
    pics = Image.objects.filter(cat=cata)

    show = {
        "catagory": catagory,
        "pics": pics

    }
    return render(request, 'home.html', show)


def red(request):
    return redirect('home')
