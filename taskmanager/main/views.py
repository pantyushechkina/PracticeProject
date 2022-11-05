from django.shortcuts import render, redirect
from .models import Contact, TypeProduct, Item


def index(request):
    return render(request, 'main/index.html')


def news(request):
    return render(request, 'main/news.html')


def news_1(request):
    return render(request, 'main/news_1.html')


def obr_sv(request):
    return render(request, 'main/obr_sv.html')


def gde_kupit(request):
    return render(request, 'main/gde_kupit.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    contactsList = Contact.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contactsList})


def catalog(request):
    items = Item.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        items = Item.objects.filter(idType = CATID)
    else:
        items = Item.objects.all()
    categories = TypeProduct.objects.all()
    return  render(request, 'main/catalog.html', {'categories': categories, 'items': items})

